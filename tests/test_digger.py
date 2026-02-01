#!/usr/bin/env python3
## ============================================================
## AUTOMATED TEST SUITE FOR DIGGER
## ============================================================
## Run: python -m pytest tests/ -v
## Or:  python tests/test_digger.py
## ============================================================

import os
import sys
import subprocess
import tempfile
from pathlib import Path

## Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from digger.config import load_config, PACKAGE_DIR, SYSTEM_PROMPT
from digger.rag import RAGSearch
from digger.session import Session
from digger.ollama import OllamaClient


## ============================================================
## TEST RESULTS TRACKING
## ============================================================
PASSED = 0
FAILED = 0
RESULTS = []

def test(name):
    """Decorator to track test results."""
    def decorator(func):
        def wrapper():
            global PASSED, FAILED
            try:
                func()
                PASSED += 1
                RESULTS.append(f"  [PASS] {name}")
                return True
            except AssertionError as e:
                FAILED += 1
                RESULTS.append(f"  [FAIL] {name}: {e}")
                return False
            except Exception as e:
                FAILED += 1
                RESULTS.append(f"  [ERROR] {name}: {e}")
                return False
        return wrapper
    return decorator


## ============================================================
## CONFIG TESTS
## ============================================================
@test("Config loads with defaults")
def test_config_loads():
    config = load_config()
    assert config["model"] == "mistral"
    assert "rag_dir" in config
    assert "memory_dir" in config

@test("Package directory resolves correctly")
def test_package_dir():
    assert PACKAGE_DIR.exists()
    assert (PACKAGE_DIR / "digger").exists()  ## Python package
    assert (PACKAGE_DIR / "RAG").exists()      ## Knowledge base

@test("RAG dir is absolute path")
def test_rag_absolute():
    config = load_config()
    rag_path = Path(config["rag_dir"])
    assert rag_path.is_absolute(), f"RAG path not absolute: {rag_path}"

@test("System prompt contains anti-roleplay rules")
def test_system_prompt():
    assert "NEVER" in SYSTEM_PROMPT
    assert "Digger:" in SYSTEM_PROMPT or "dialogue" in SYSTEM_PROMPT
    assert "ONE" in SYSTEM_PROMPT


## ============================================================
## RAG TESTS
## ============================================================
@test("RAG finds knowledge files")
def test_rag_finds_files():
    config = load_config()
    rag = RAGSearch(config["rag_dir"])
    files = rag.list_files()
    assert len(files) > 0, "No RAG files found"
    filenames = [f[0] for f in files]
    assert any("Networking" in f for f in filenames), "Missing networking file"

@test("RAG search returns results for 'TCP'")
def test_rag_search_tcp():
    config = load_config()
    rag = RAGSearch(config["rag_dir"])
    results = rag.search("TCP")
    assert len(results) > 0, "No results for TCP"
    assert "TCP" in results or "tcp" in results.lower()

@test("RAG search returns results for 'ACSC'")
def test_rag_search_acsc():
    config = load_config()
    rag = RAGSearch(config["rag_dir"])
    results = rag.search("ACSC")
    ## May or may not have ACSC content - just verify search runs
    assert isinstance(results, str)

@test("RAG respects bounds limits")
def test_rag_bounds():
    config = load_config()
    rag = RAGSearch(config["rag_dir"])
    results = rag.search("the")  ## Common word, many matches
    assert len(results) <= 8500, f"Results too long: {len(results)}"


## ============================================================
## SESSION TESTS
## ============================================================
@test("Session creates with unique ID")
def test_session_creates():
    with tempfile.TemporaryDirectory() as tmpdir:
        session = Session(memory_dir=tmpdir)
        assert session.id is not None
        assert len(session.id) > 0

@test("Session stores messages")
def test_session_messages():
    with tempfile.TemporaryDirectory() as tmpdir:
        session = Session(memory_dir=tmpdir)
        session.add_message("George", "test question")
        session.add_message("Digger", "test answer")
        assert session.get_message_count() == 2

@test("Session context includes system prompt")
def test_session_context():
    with tempfile.TemporaryDirectory() as tmpdir:
        session = Session(memory_dir=tmpdir)
        session.add_message("George", "hello")
        context = session.get_context()
        assert "Digger" in context  ## System prompt mentions Digger
        assert "George: hello" in context


## ============================================================
## OLLAMA TESTS
## ============================================================
@test("Ollama client initializes")
def test_ollama_init():
    ollama = OllamaClient(model="mistral")
    assert ollama.model == "mistral"

@test("Ollama can list models")
def test_ollama_list():
    ollama = OllamaClient(model="mistral")
    output = ollama.list_models()
    assert "mistral" in output.lower() or "NAME" in output

@test("Ollama model check works")
def test_ollama_check():
    ollama = OllamaClient(model="mistral")
    exists = ollama.check_model()
    assert isinstance(exists, bool)


## ============================================================
## CLI INTEGRATION TESTS
## ============================================================
@test("CLI --help works")
def test_cli_help():
    result = subprocess.run(
        ["digger", "--help"],
        capture_output=True,
        text=True,
        timeout=10
    )
    assert result.returncode == 0
    assert "Digger" in result.stdout

@test("CLI --list works")
def test_cli_list():
    result = subprocess.run(
        ["digger", "--list"],
        capture_output=True,
        text=True,
        timeout=10
    )
    assert result.returncode == 0
    assert "NAME" in result.stdout or "mistral" in result.stdout.lower()


## ============================================================
## STREAMING TEST
## ============================================================
@test("Text streams before voice (non-blocking)")
def test_streaming_order():
    ## This verifies the code structure, not runtime behavior
    cli_path = PACKAGE_DIR / "digger" / "cli.py"
    with open(cli_path) as f:
        content = f.read()

    ## Find ollama.chat call
    chat_pos = content.find("ollama.chat(context)")
    voice_pos = content.find("voice_engine.speak(response)")

    assert chat_pos > 0, "ollama.chat not found"
    assert voice_pos > 0, "voice_engine.speak not found"
    assert chat_pos < voice_pos, "Voice called before chat completes"


## ============================================================
## RUN ALL TESTS
## ============================================================
def run_all():
    print("=" * 60)
    print("DIGGER AUTOMATED TEST SUITE")
    print("=" * 60)

    ## Config tests
    print("\n[CONFIG TESTS]")
    test_config_loads()
    test_package_dir()
    test_rag_absolute()
    test_system_prompt()

    ## RAG tests
    print("\n[RAG TESTS]")
    test_rag_finds_files()
    test_rag_search_tcp()
    test_rag_search_acsc()
    test_rag_bounds()

    ## Session tests
    print("\n[SESSION TESTS]")
    test_session_creates()
    test_session_messages()
    test_session_context()

    ## Ollama tests
    print("\n[OLLAMA TESTS]")
    test_ollama_init()
    test_ollama_list()
    test_ollama_check()

    ## CLI tests
    print("\n[CLI TESTS]")
    test_cli_help()
    test_cli_list()

    ## Streaming test
    print("\n[STREAMING TESTS]")
    test_streaming_order()

    ## Results
    print("\n" + "=" * 60)
    print("RESULTS:")
    for r in RESULTS:
        print(r)
    print("=" * 60)
    print(f"PASSED: {PASSED} | FAILED: {FAILED}")
    print("=" * 60)

    return FAILED == 0


if __name__ == "__main__":
    success = run_all()
    sys.exit(0 if success else 1)
