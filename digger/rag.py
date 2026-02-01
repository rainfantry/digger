## ============================================================
## RAG.PY - Retrieval Augmented Generation search engine
## ============================================================
## Searches knowledge base (.md files) for relevant content.
##
## BOUNDS LIMITS (prevent context overflow):
## - MAX_MATCHES_PER_FILE: Max matching sections per file
## - MAX_CONTEXT_LINES: Lines of context around each match
## - APPROX_CHAR_LIMIT: Total character limit (~2000 tokens)
## - MAX_FILES: Maximum number of files to include
##
## These limits prevent small models from choking on huge context.
## ============================================================

import os
import glob
import re
from pathlib import Path


## ============================================================
## BOUNDS LIMITS - Prevent context overflow
## ============================================================
MAX_MATCHES_PER_FILE = 3      ## Max matching sections per file
MAX_CONTEXT_LINES = 5         ## Lines before/after each match
APPROX_CHAR_LIMIT = 8000      ## ~2000 tokens max total
MAX_FILES = 5                 ## Max files to include in results


class RAGSearch:
    """
    Search engine for RAG knowledge base.

    Example:
        rag = RAGSearch("./RAG")
        results = rag.search("TCP")
        print(results)
    """

    def __init__(self, rag_dir="./RAG"):
        """
        Initialize RAG search.

        Args:
            rag_dir: Directory containing .md knowledge files
        """
        self.rag_dir = Path(rag_dir)

        ## Create directory if it doesn't exist
        self.rag_dir.mkdir(parents=True, exist_ok=True)

    def search(self, topic):
        """
        Search all .md files for a topic.

        Args:
            topic: Search term (case insensitive)

        Returns:
            str: Formatted results with source labels, or empty string

        Example output:
            [SOURCE: networking.md]
            TCP is a connection-based protocol...

            [SOURCE: protocols.md]
            TCP provides reliable delivery...
        """
        if not topic or not topic.strip():
            return ""

        topic = topic.strip()
        results = []
        total_chars = 0
        files_included = 0

        ## Find all .md files
        md_files = sorted(glob.glob(str(self.rag_dir / "*.md")))

        if not md_files:
            return ""

        ## Search each file
        for filepath in md_files:
            ## Check if we've hit limits
            if files_included >= MAX_FILES:
                break
            if total_chars >= APPROX_CHAR_LIMIT:
                break

            ## Search this file
            matches = self._search_file(filepath, topic)

            if matches:
                ## Check if adding this would exceed limit
                if total_chars + len(matches) > APPROX_CHAR_LIMIT:
                    ## Truncate to fit
                    remaining = APPROX_CHAR_LIMIT - total_chars
                    if remaining > 200:  ## Only include if meaningful
                        matches = matches[:remaining] + "\n[...truncated...]"
                    else:
                        break

                filename = os.path.basename(filepath)
                formatted = f"[SOURCE: {filename}]\n{matches}"
                results.append(formatted)
                total_chars += len(formatted)
                files_included += 1

        return "\n\n".join(results)

    def _search_file(self, filepath, topic):
        """
        Search a single file for topic matches.

        Returns matching lines with context (lines before/after).

        Args:
            filepath: Path to .md file
            topic: Search term

        Returns:
            str: Matching content with context, or empty string
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Warning: Could not read {filepath}: {e}")
            return ""

        ## Find matching line numbers (case insensitive)
        pattern = re.compile(re.escape(topic), re.IGNORECASE)
        match_indices = []

        for i, line in enumerate(lines):
            if pattern.search(line):
                match_indices.append(i)

        if not match_indices:
            return ""

        ## Limit matches per file
        match_indices = match_indices[:MAX_MATCHES_PER_FILE]

        ## Extract matches with context
        extracted = []
        seen_ranges = set()  ## Avoid duplicate lines

        for idx in match_indices:
            ## Calculate context range
            start = max(0, idx - MAX_CONTEXT_LINES)
            end = min(len(lines), idx + MAX_CONTEXT_LINES + 1)

            ## Extract lines we haven't seen
            section_lines = []
            for i in range(start, end):
                if i not in seen_ranges:
                    seen_ranges.add(i)
                    section_lines.append(lines[i].rstrip())

            if section_lines:
                extracted.append("\n".join(section_lines))

        return "\n--\n".join(extracted)

    def list_files(self):
        """
        List all knowledge base files.

        Returns:
            list: List of (filename, line_count, size_kb) tuples
        """
        files = []
        md_files = glob.glob(str(self.rag_dir / "*.md"))

        for filepath in sorted(md_files):
            try:
                filename = os.path.basename(filepath)
                line_count = sum(1 for _ in open(filepath))
                size_kb = os.path.getsize(filepath) / 1024
                files.append((filename, line_count, f"{size_kb:.1f}KB"))
            except Exception:
                pass

        return files

    def get_file_content(self, filename):
        """
        Get full content of a specific file.

        Args:
            filename: Name of file (e.g., "networking.md")

        Returns:
            str: File content or error message
        """
        filepath = self.rag_dir / filename

        if not filepath.exists():
            return f"File not found: {filename}"

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error reading {filename}: {e}"

    def add_note(self, note, filename="general_notes.md"):
        """
        Add a note to the knowledge base.

        Args:
            note: The note content
            filename: Target file (default: general_notes.md)
        """
        from datetime import datetime

        filepath = self.rag_dir / filename

        ## Append with timestamp
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"{note}\n")

    def get_stats(self):
        """
        Get statistics about the knowledge base.

        Returns:
            dict: Stats about files, size, etc.
        """
        md_files = glob.glob(str(self.rag_dir / "*.md"))
        total_lines = 0
        total_size = 0

        for filepath in md_files:
            try:
                total_lines += sum(1 for _ in open(filepath))
                total_size += os.path.getsize(filepath)
            except Exception:
                pass

        return {
            "file_count": len(md_files),
            "total_lines": total_lines,
            "total_size_kb": f"{total_size / 1024:.1f}KB",
            "rag_dir": str(self.rag_dir),
        }


## ============================================================
## QUICK TEST - Run this file directly to test RAG search
## ============================================================
if __name__ == "__main__":
    import sys

    ## Use actual RAG directory for testing
    rag_dir = "/home/recon/TAFE/TEACHER_BETA/RAG"

    print("Testing RAG search...")
    print("=" * 50)

    rag = RAGSearch(rag_dir)

    ## Show stats
    print("\n--- Knowledge Base Stats ---")
    stats = rag.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    ## List files
    print("\n--- Files ---")
    for filename, lines, size in rag.list_files():
        print(f"  {filename} ({lines} lines, {size})")

    ## Test search
    topic = sys.argv[1] if len(sys.argv) > 1 else "ACSC"
    print(f"\n--- Search: '{topic}' ---")
    results = rag.search(topic)

    if results:
        ## Show truncated preview
        preview = results[:1000] + "..." if len(results) > 1000 else results
        print(preview)
        print(f"\n[Total: {len(results)} chars]")
    else:
        print("No results found.")

    print("\n" + "=" * 50)
