## ============================================================
## SESSION.PY - Session and memory management
## ============================================================
## Handles conversation history and persistence.
##
## What this does:
## 1. Creates a unique session ID (timestamp)
## 2. Tracks all messages (George + Digger)
## 3. Stores RAG context that was loaded
## 4. Saves everything to a file for persistence
## 5. Provides the full context to send to the model
##
## The model sees: RAG content + conversation history
## ============================================================

import os
from datetime import datetime
from pathlib import Path

from digger.config import SYSTEM_PROMPT


class Session:
    """
    Manages a single study session.

    Example:
        session = Session(memory_dir="./memory")
        session.add_context("TCP is a protocol...")   # Add RAG content
        session.add_message("George", "what is TCP")  # Add user message
        session.add_message("Digger", "TCP is...")    # Add model response

        context = session.get_context()  # Get full context for model
    """

    def __init__(self, memory_dir="./memory"):
        """
        Initialize a new session.

        Args:
            memory_dir: Directory to store session files
        """
        ## Create unique session ID from timestamp
        ## Format: YYYYMMDD_HHMMSS (e.g., 20260121_143052)
        self.id = datetime.now().strftime("%Y%m%d_%H%M%S")

        ## Setup paths
        self.memory_dir = Path(memory_dir)
        self.filepath = self.memory_dir / f"session_{self.id}.txt"

        ## Ensure memory directory exists
        self.memory_dir.mkdir(parents=True, exist_ok=True)

        ## Initialize context storage
        ## _rag_context: Knowledge loaded from RAG files
        ## _messages: List of (role, content) tuples
        self._rag_context = ""
        self._messages = []

        ## Create empty session file
        self._save()

    def add_context(self, content, topic=""):
        """
        Add RAG knowledge to the session context.

        This content will be included at the START of what the model sees,
        so it has the knowledge available when answering questions.

        Args:
            content: The RAG content to add
            topic: Optional topic label for logging
        """
        if not content:
            return

        ## Format with clear markers so model knows this is reference material
        formatted = f"\n=== KNOWLEDGE ON '{topic}' ===\n{content}\n=== END KNOWLEDGE ===\n"

        self._rag_context += formatted
        self._save()

    def add_message(self, role, content):
        """
        Add a message to the conversation history.

        Args:
            role: Who said it ("George" or "Digger")
            content: What was said
        """
        if not content or not content.strip():
            return

        self._messages.append((role, content.strip()))
        self._save()

    def get_context(self):
        """
        Get the full context to send to the model.

        Returns:
            str: System prompt + RAG content + conversation history

        The format is:
            [SYSTEM PROMPT]
            You are Digger...

            [RAG KNOWLEDGE]
            === KNOWLEDGE ON 'topic' ===
            ... content ...
            === END KNOWLEDGE ===

            [CONVERSATION]
            George: question
            Digger: answer
            George: next question
        """
        ## Build context string
        context_parts = []

        ## Add system prompt FIRST (sets personality)
        context_parts.append(SYSTEM_PROMPT)

        ## Add RAG context (so model has knowledge before questions)
        if self._rag_context:
            context_parts.append(self._rag_context)

        ## Add conversation history
        for role, content in self._messages:
            context_parts.append(f"{role}: {content}")

        return "\n".join(context_parts)

    def get_last_message(self, role=None):
        """
        Get the last message, optionally filtered by role.

        Args:
            role: Filter by role ("George" or "Digger") or None for any

        Returns:
            str: The last message content, or empty string
        """
        for msg_role, content in reversed(self._messages):
            if role is None or msg_role == role:
                return content
        return ""

    def get_message_count(self):
        """
        Get the number of messages in the conversation.

        Returns:
            int: Number of messages
        """
        return len(self._messages)

    def clear_context(self):
        """
        Clear RAG context but keep conversation history.

        Useful if context gets too long.
        """
        self._rag_context = ""
        self._save()

    def _save(self):
        """
        Save the current session to disk.

        Called automatically after each modification.
        """
        try:
            with open(self.filepath, "w") as f:
                ## Write session header
                f.write(f"## Session: {self.id}\n")
                f.write(f"## Started: {datetime.now().isoformat()}\n")
                f.write("\n")

                ## Write RAG context
                if self._rag_context:
                    f.write("## === RAG CONTEXT ===\n")
                    f.write(self._rag_context)
                    f.write("\n")

                ## Write conversation
                f.write("## === CONVERSATION ===\n")
                for role, content in self._messages:
                    f.write(f"{role}: {content}\n")

        except Exception as e:
            print(f"Warning: Could not save session: {e}")

    def get_summary(self):
        """
        Get a summary of the session for display.

        Returns:
            dict: Session info
        """
        return {
            "id": self.id,
            "filepath": str(self.filepath),
            "message_count": len(self._messages),
            "has_rag_context": bool(self._rag_context),
            "rag_context_length": len(self._rag_context),
        }


## ============================================================
## QUICK TEST - Run this file directly to test session management
## ============================================================
if __name__ == "__main__":
    print("Testing session management...")
    print("=" * 50)

    ## Create a test session
    session = Session(memory_dir="./test_memory")

    ## Add some RAG context
    session.add_context("TCP is a reliable transport protocol.", topic="TCP")

    ## Add conversation
    session.add_message("George", "what is TCP")
    session.add_message("Digger", "TCP is a protocol that guarantees delivery, ya drongo.")
    session.add_message("George", "thanks dickhead")

    ## Get context
    print("\n--- Full Context ---")
    print(session.get_context())

    ## Show summary
    print("\n--- Summary ---")
    for key, value in session.get_summary().items():
        print(f"  {key}: {value}")

    print("\n" + "=" * 50)
    print(f"Session saved to: {session.filepath}")
