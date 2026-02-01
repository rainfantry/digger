#!/usr/bin/env python3
## ============================================================
## CLI.PY - Main entry point for Digger
## ============================================================
## This is the main file that ties everything together.
##
## FLOW:
## 1. Parse command line arguments
## 2. Load configuration (CLI > env > yaml > defaults)
## 3. Initialize components (session, ollama, voice, rag)
## 4. Show banner
## 5. Main loop:
##    - Read user input
##    - Check for commands (exit, load, paste, etc.)
##    - Send to model
##    - Play voice response
## 6. Handle Ctrl+C for voice skip
##
## USAGE:
##   digger                    # Default model
##   digger --model mistral    # Specific model
##   digger --no-voice         # Disable voice
##   digger --list             # List models
## ============================================================
print("*** PORT-TEST VERSION RUNNING - STARTUP CHECK ***")
import argparse
import sys
import readline  ## Enables arrow keys in input()

from digger.config import load_config
from digger.session import Session
from digger.ollama import OllamaClient
from digger.voice import VoiceEngine
from digger.rag import RAGSearch


## ============================================================
## GLOBALS
## ============================================================
voice_engine = None


def print_banner(session_id, model, rag_dir):
    """
    Print the startup banner.
    """
    banner = r"""
 _____                                                                 _____
( ___ )                                                               ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   |
 |   |       22nd Survey Division ABN 50 692 429 397 Presents:         |   |
 |   | ____ ____ ____ ____ ____ ____ . ____    _  _ ____ _  _ ___ _  _ |   |
 |   | | __ |___ |  | |__/ | __ |___ ' [__     |\/| |  | |  |  |  |__| |   |
 |   | |__] |___ |__| |  \ |__] |___   ___]    |  | |__| |__|  |  |  | |   |
 |   |                                                                 |   |
 |   | _  _ _  _ _ _    ____ _  _ ____ _  _ ____ _   _    ___  _ _  _  |   |
 |   |  \/   \/  | |    [__  |  | |__/ |  | |___  \_/     |  \ | |  |  |   |
 |   | _/\_ _/\_ | |    ___] |__| |  \  \/  |___   |      |__/ |  \/   |   |
 |   |                                                                 |   |
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___|
(_____)                                                               (_____)
"""
    print(banner)
    print("DIGGER - Foul-mouthed Aussie Study Assistant")
    print(f"Session: {session_id} | Model: {model}")
    print(f"Knowledge: {rag_dir}")
    print("")
    print("Commands: exit | clear | load <topic> | paste | help")
    print("Ctrl+C = skip voice | Type 'exit' to quit")
    print("=" * 60)


def print_help():
    """
    Print help information.
    """
    print("""
DIGGER COMMANDS
────────────────────────────────────────────────────────────
  exit                    - End session (saves memory)
  clear                   - Reset session (clears history + RAG)
  paste                   - Multiline input (blank line to send)
  load <topic>            - Search RAG for topic
  remember <note>         - Add to general_notes.md
  remember <file>: <note> - Add to specific file
  show files              - List all RAG files
  show knowledge          - Display RAG stats
  help                    - Show this message
────────────────────────────────────────────────────────────
Ctrl+C skips voice playback. Type 'exit' to quit.
""")


def multiline_input():
    """
    Collect multiline input until blank line.

    Returns:
        str: All lines joined, or empty string if cancelled
    """
    print("")
    print("MULTILINE INPUT MODE")
    print("Type your message (blank line to send):")
    print("────────────────────────────────────────")

    lines = []
    try:
        while True:
            line = input("│ ")
            if not line:  ## Blank line = done
                break
            lines.append(line)
    except EOFError:
        pass

    print("────────────────────────────────────────")

    if lines:
        return "\n".join(lines)
    else:
        print("(empty - cancelled)")
        return ""


def main():
    """
    Main entry point for Digger CLI.
    """
    global voice_engine

    ## ========================================
    ## STEP 1: Parse command line arguments
    ## ========================================
    parser = argparse.ArgumentParser(
        description="Digger - Foul-mouthed Aussie study assistant"
    )
    parser.add_argument(
        "--model", "-m",
        help="Ollama model name (default: from config)"
    )
    parser.add_argument(
        "--no-voice",
        action="store_true",
        help="Disable voice output"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List available Ollama models"
    )
    parser.add_argument(
        "--rag-dir",
        help="RAG knowledge base directory"
    )
    parser.add_argument(
        "--memory-dir",
        help="Session memory directory"
    )

    args = parser.parse_args()

    ## ========================================
    ## STEP 2: Load configuration
    ## ========================================
    config = load_config(args)

    ## Handle --list flag
    if args.list:
        ollama = OllamaClient(config["model"])
        print(ollama.list_models())
        return

    ## ========================================
    ## STEP 3: Initialize components
    ## ========================================

    ## Session for memory management
    session = Session(memory_dir=config["memory_dir"])

    ## Ollama client for model interaction
    ollama = OllamaClient(model=config["model"])

    ## Voice engine (if enabled)
    if config["voice_enabled"] and not args.no_voice:
        voice_engine = VoiceEngine(config)
    else:
        voice_engine = None

    ## RAG search engine
    rag = RAGSearch(rag_dir=config["rag_dir"])

    ## ========================================
    ## STEP 4: Show banner
    ## ========================================
    print_banner(session.id, config["model"], config["rag_dir"])

    ## Startup voice
    if voice_engine:
        voice_engine.speak("Alright motherfucker lets address this quick. Thank you everybody for helpin out, thank you Grok! Thank you Claude you both real nigguhs for troubleshootin my shit and first and foremost. Thank myself, shit. Thought I was gonna thank you nigguh? now. I just wanna say. Look, fuck you, fuck the plane you flew in on, fuck them shoes, fuck those socks with the belt on it, fuck your gay-ass fairy faggot accent, fuck them cheap-ass cigars, fuck your yuck-mouth teeth, fuck your hairpiece, fuck your chocolate, fuck Guy Ritchie, fuck Prince William, fuck the Queen. This is Australia! nigga. Now, get the fuck out my hotel roomand if I see you in the street, I'm slapping the shit out of you.")

    ## ========================================
    ## STEP 5: Main loop
    ## ========================================
    ## Simple loop: Ctrl+C skips voice or returns to prompt
    ## No complex signal handling - let Python do it naturally
    while True:
        try:
            ## Get user input
            print("")
            user_input = input("You> ").strip()

            ## Skip empty input
            if not user_input:
                continue

            ## ====== COMMAND: exit ======
            if user_input.lower() in ("exit", "quit", "bye"):
                print("")
                print("SESSION SUMMARY")
                print(f"Session file: {session.filepath}")
                summary = session.get_summary()
                print(f"Messages: {summary['message_count']}")
                print("")

                if voice_engine:
                    voice_engine.speak("Session complete.")
                    voice_engine.wait()

                print("Session ended. Memory preserved.")
                break

            ## ====== COMMAND: help ======
            if user_input.lower() == "help":
                print_help()
                continue

            ## ====== COMMAND: clear ======
            if user_input.lower() == "clear":
                session._messages = []
                session._rag_context = ""
                session._save()
                print("Session cleared. RAG and history reset.")
                continue

            ## ====== COMMAND: paste ======
            if user_input.lower() == "paste":
                user_input = multiline_input()
                if not user_input:
                    continue
                ## Fall through to send to model

            ## ====== COMMAND: load <topic> ======
            if user_input.lower().startswith("load "):
                topic = user_input[5:].strip()
                if not topic:
                    print("Usage: load <topic>")
                    continue

                print(f"\nSearching knowledge base for: {topic}")
                print("─" * 50)

                results = rag.search(topic)

                if results:
                    print(results[:2000])  ## Show first 2000 chars
                    if len(results) > 2000:
                        print(f"\n[...{len(results) - 2000} more chars...]")
                    print("─" * 50)

                    ## Add to session context
                    session.add_context(results, topic=topic)
                    print(f"\nKnowledge loaded into session context.")

                    if voice_engine:
                        voice_engine.speak(f"Knowledge loaded on {topic}.")
                else:
                    print(f"No knowledge found on '{topic}'.")
                    print("\nAvailable files:")
                    for filename, lines, size in rag.list_files():
                        print(f"  {filename} ({lines} lines)")

                continue

            ## ====== COMMAND: remember ======
            if user_input.lower().startswith("remember "):
                note = user_input[9:].strip()
                if not note:
                    print("Usage: remember <note>")
                    print("   or: remember <file>: <note>")
                    continue

                ## Check for file:note format
                if ": " in note:
                    parts = note.split(": ", 1)
                    filename = parts[0].strip() + ".md"
                    note_text = parts[1].strip()
                else:
                    filename = "general_notes.md"
                    note_text = note

                rag.add_note(note_text, filename)
                print(f"Added to: {filename}")

                if voice_engine:
                    voice_engine.speak("Note added.")

                continue

            ## ====== COMMAND: show files ======
            if user_input.lower() == "show files":
                print("\nKNOWLEDGE BASE FILES:")
                print("═" * 50)
                files = rag.list_files()
                if files:
                    for filename, lines, size in files:
                        print(f"  {filename} ({lines} lines, {size})")
                else:
                    print("  (no files yet - use 'remember' to create)")
                print("═" * 50)
                continue

            ## ====== COMMAND: show knowledge ======
            if user_input.lower() == "show knowledge":
                stats = rag.get_stats()
                print("\nKNOWLEDGE BASE STATS:")
                print("═" * 50)
                for key, value in stats.items():
                    print(f"  {key}: {value}")
                print("═" * 50)
                continue

            ## ====================================
            ## DEFAULT: Send to model
            ## ====================================

            ## Final safety check - don't send garbage to model
            if not user_input or not user_input.strip():
                continue

            ## Add user message to session
            session.add_message("George", user_input)

            ## Get full context (RAG + conversation)
            context = session.get_context()

            ## Send to model
            print("")
            print("Digger:")
            print("─" * 50)

            try:
                response = ollama.chat(context)
                print("")  ## Ensure newline after streaming
            except KeyboardInterrupt:
                print("\n[Interrupted]")
                response = ""

            print("─" * 50)

            ## Save response to session
            if response:
                session.add_message("Digger", response)

                ## Voice output (non-blocking)
                if voice_engine:
                    voice_engine.speak(response)

        except EOFError:
            ## Ctrl+D pressed
            print("\n[EOF - exiting]")
            break

        except KeyboardInterrupt:
            ## Ctrl+C - skip voice if playing, return to prompt
            if voice_engine:
                voice_engine.skip()
            print("")
            ## Reset readline line buffer (not history)
            try:
                readline.set_pre_input_hook(None)
                readline.redisplay()
            except:
                pass
            try:
                import termios
                termios.tcflush(sys.stdin, termios.TCIFLUSH)
            except:
                pass
            continue

    ## ========================================
    ## CLEANUP
    ## ========================================
    if voice_engine:
        voice_engine.skip()

    print("")
    print("=" * 60)


## ============================================================
## ENTRY POINT
## ============================================================
if __name__ == "__main__":
    main()
