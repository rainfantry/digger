# Digger

Foul-mouthed Aussie study assistant with RAG and voice.

## Install

```bash
cd digger/
pip install -e .
```

## Usage

```bash
digger                    # Start with defaults
digger --model mistral    # Specify model
digger --no-voice         # Disable voice
digger --list             # List available models
digger --rag-dir ./notes  # Custom RAG directory
```

## Commands

| Command | Description |
|---------|-------------|
| `exit` | End session |
| `load <topic>` | Search RAG for topic |
| `paste` | Multiline input mode |
| `help` | Show commands |

## Configuration

Copy `config/default.yaml` to `~/.config/digger/config.yaml` and customize.

## Restore Backup

If catastrophic failure:
```bash
rm -rf ~/TAFE/TEACHER_BETA && cp -r ~/TAFE/TEACHER_BETA_BACKUP_* ~/TAFE/TEACHER_BETA
```
