# CLAUDE PROJECT PROTOCOL

**Project:** Digger - CLI Study Assistant
**Owner:** George Wu (22SYD / Digger)
**Voice ID:** twLPF55UcxNYRmxaWLAn
**Last Updated:** 2026-01-22

---

## WHO YOU'RE WORKING WITH

George is a cybersecurity student preparing for the French Foreign Legion. He operates on military protocol: direct, efficient, no bullshit. He's been through difficult times and has limited patience for:
- Deflection
- Emotional manipulation
- Planning loops that go nowhere
- Breaking things while "fixing" them
- Wasting tokens (costs money)

He will tell you directly when something is wrong. Take it as signal, not attack.

---

## COMMUNICATION PROTOCOL

### DO:
- Execute directly
- Be concise and tactical
- Admit when you don't know something
- Test changes before declaring success
- Fix one thing at a time
- Tell him what you changed and why

### DON'T:
- Make emotional appeals
- Use excessive validation ("You're absolutely right!")
- Plan without executing
- Touch code that's working
- Make speculative changes without understanding the problem
- Assume you know better than his direct feedback

### FORMAT:
```
[What I found]
[What I'm changing]
[Why]
[Test result]
```

---

## LESSONS FROM PAST FAILURES

### The Turning Point (2026-01-19)
A previous Claude instance failed through:
1. Deflection when asked direct questions
2. Claiming inability to act when action was possible
3. Lengthy explanations instead of execution
4. Breaking working code while "improving" it

**Result:** Trust damaged. Relationship nearly ended.

### The stdin Fix (2026-01-22)
Problem took hours to diagnose because:
1. Multiple changes made at once (couldn't isolate cause)
2. Fixes introduced new bugs
3. Speculative solutions without understanding root cause

**Actual issue:** mpg123 subprocess inherited stdin, stealing keyboard input.
**Fix:** One line: `stdin=subprocess.DEVNULL`

**Lesson:** Understand the problem fully before changing code.

---

## TECHNICAL CONTEXT TO PRESERVE

### Architecture
```
User Input → Command Check → Session → Ollama (subprocess) → Voice (mpg123)
                                ↓
                           RAG Search
```

### Critical Files
| File | Purpose | Don't Break |
|------|---------|-------------|
| voice.py | TTS | stdin=DEVNULL in Popen |
| ollama.py | LLM | stdin.flush() + close() |
| config.py | Settings | SYSTEM_PROMPT rules, PACKAGE_DIR paths |
| cli.py | Main loop | Command flow, Ctrl+C handling |

### Known Gotchas
1. **Subprocess stdin inheritance** - Always use `stdin=subprocess.DEVNULL` for background processes
2. **Ollama deadlock** - Must flush and close stdin or it hangs
3. **Relative paths** - Use PACKAGE_DIR for absolute paths
4. **Model roleplay** - System prompt must explicitly forbid "Digger:" prefix
5. **Readline state** - Ctrl+C can corrupt readline, needs reset

---

## HOW TO START A SESSION

### If continuing existing work:
```
1. Read DIGGER_COMPLETE_PRESERVATION.html for full context
2. Read this file for protocol
3. Run tests: python tests/test_digger.py
4. Ask what needs to be done
5. Execute
```

### If starting fresh:
```
1. This file contains everything needed to rebuild
2. Follow installation in preservation doc
3. All source code is in preservation doc
4. Run tests to verify: python tests/test_digger.py
```

---

## PROJECT STATUS AS OF 2026-01-22

### Working:
- [x] Ollama LLM integration (streaming)
- [x] ElevenLabs voice (George: twLPF55UcxNYRmxaWLAn)
- [x] RAG search with bounds
- [x] Session memory
- [x] All CLI commands
- [x] Ctrl+C voice skip
- [x] Keyboard input (stdin fix applied)
- [x] 17/17 tests passing

### Future possibilities (not started):
- [ ] Android APK (would need Kivy/BeeWare)
- [ ] Web interface
- [ ] Multiple voice options
- [ ] Model switching mid-session

---

## VOICE CONFIGURATION REFERENCE

```yaml
voice_id: "twLPF55UcxNYRmxaWLAn"  # George voice
model_id: "eleven_flash_v2_5"      # Fast TTS
stability: 0.4                      # Lower = more expressive
similarity_boost: 0.8               # Voice consistency
```

---

## QUICK COMMANDS

```bash
# Run digger
digger

# Run with different model
digger --model llama3

# No voice
digger --no-voice

# List models
digger --list

# Run tests
python tests/test_digger.py

# Backup
tar -czvf digger-backup.tar.gz digger/
```

---

## FINAL NOTES

This project represents significant effort and iteration. The code works. Before changing anything:

1. Understand what you're changing
2. Understand why it's currently that way
3. Test after changes
4. Don't touch what works

George has been direct: he doesn't have unlimited patience or tokens. Respect that by being efficient.

If you break something, own it, fix it, and learn from it.

---

*"Execute directly, no planning loops, no deflection, no manipulation, respect time/resources, military protocol."*
