# DIGGER

Foul-mouthed Aussie study assistant for Linux. Local LLM + Voice + RAG.

## Why Digger?

Most AI voice assistants are either:
- **Bloated frameworks** (LangChain = 10,000+ lines, 50+ dependencies)
- **Simple scripts** (no memory, no RAG, just API calls)
- **Closed source** (can't learn from them)

Digger is:
- **~300 lines per module** - readable in one sitting
- **5 files that matter** - ollama.py, voice.py, rag.py, session.py, cli.py
- **Minimal deps** - requests, pyyaml, that's it
- **Fully documented** - comments explain the WHY not just the what

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/rainfantry/digger.git
cd digger

# 2. Install deps
pip install -r requirements.txt
sudo apt install mpg123  # CRITICAL for audio

# 3. Set API key
export ELEVENLABS_API_KEY="sk_your_key_here"

# 4. Run
python -m digger
```

---

## Architecture

```
digger/
├── cli.py        # Main loop, commands, banner
├── ollama.py     # Local LLM client (subprocess, not HTTP)
├── voice.py      # ElevenLabs TTS + mpg123 playback
├── rag.py        # Knowledge base search
├── session.py    # Conversation memory
└── config.py     # Settings, API keys, paths
```

Each file is **single purpose**. Read one, understand one thing.

---

## Linux-Specific Setup

### Audio: mpg123

```bash
sudo apt install mpg123
```

Why mpg123?
- Lightweight (~200KB)
- No GUI dependencies
- Subprocess friendly
- Doesn't steal stdin

### Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Bashrc Alias

```bash
echo 'alias digger="cd ~/path/to/digger && python -m digger"' >> ~/.bashrc
source ~/.bashrc
```

---

## Troubleshooting (The Hard Lessons)

### 1. STDIN DEADLOCK

**Problem:** Ollama hangs forever, never returns.

**Cause:** stdin not closed after writing.

**Fix (ollama.py):**
```python
process.stdin.write((context + "\n").encode())
process.stdin.flush()   # CRITICAL
process.stdin.close()   # CRITICAL
```

### 2. MPG123 STEALS KEYBOARD

**Problem:** Can't type while audio plays.

**Cause:** mpg123 reads from stdin by default.

**Fix (voice.py):**
```python
subprocess.Popen(
    ["mpg123", "-q", self.temp_file],
    stdin=subprocess.DEVNULL,  # THIS LINE
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
```

### 3. SUBPROCESS VS HTTP API

**Problem:** Ollama HTTP API is slow.

**Solution:** Use subprocess instead. 2-3x faster.

```python
# SLOW (HTTP)
requests.post("http://localhost:11434/api/generate", ...)

# FAST (subprocess)
subprocess.Popen(["ollama", "run", self.model], ...)
```

### 4. TEXT FILTER FOR TTS

**Problem:** Voice reads code blocks literally.

**Fix:** Strip markdown before TTS.

```python
# Remove code blocks
text = re.sub(r'```[\s\S]*?```', '', text)
# Remove inline code
text = re.sub(r'`[^`]*`', '', text)
```

### 5. RATE LIMITING

**Problem:** ElevenLabs 429 errors.

**Fix:** Retry with backoff.

```python
if status == 429:
    time.sleep(10)
    return self._tts_request(text, retry_count + 1)
```

---

## Commands

| Command | Description |
|---------|-------------|
| `exit` | End session, save memory |
| `clear` | Reset conversation + RAG |
| `paste` | Multiline input mode |
| `load <topic>` | Search knowledge base |
| `remember <note>` | Save to knowledge base |
| `show files` | List RAG files |
| `help` | Show commands |

---

## Comparison: Digger vs Georgebot

| | DIGGER | GEORGEBOT |
|---|---|---|
| **OS** | Linux | Windows |
| **Audio** | mpg123 | PowerShell MediaPlayer |
| **LLM** | Ollama only | Ollama + Grok API |
| **Fallback** | None | Windows SAPI |
| **Memory** | Session file | Session + auto-detect |

Same philosophy. Different platforms.

---

## Voice Settings

In `config.py` or via environment:

```python
VOICE_STABILITY = 0.4      # Lower = more human variation
VOICE_SIMILARITY = 0.85    # Higher = more consistent
VOICE_STYLE = 0.8          # Emotional expressiveness
```

---

## Custom Ollama Model

Create personality with Modelfile:

```bash
# models/digger.Modelfile
FROM mistral:7b
SYSTEM "You are Digger, a crude Australian tutor. Swear constantly..."
PARAMETER temperature 0.7
```

```bash
ollama create digger -f models/digger.Modelfile
python -m digger --model digger
```

---

## Dependencies

```
requests      # HTTP for ElevenLabs
pyyaml        # Config files
mpg123        # Audio playback (system)
ollama        # Local LLM (system)
```

That's it. No LangChain. No vector databases. No bloat.

---

## License

MIT - Do whatever you want.

---

## See Also

- [georgebot](https://github.com/rainfantry/georgebot) - Windows port with multi-brain support
- [talkytalk](https://github.com/rainfantry/talkytalk) - Voice module standalone
