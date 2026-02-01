## ============================================================
## CONFIG.PY - Configuration management
## ============================================================
## Handles loading and merging configuration from multiple sources.
##
## PRECEDENCE CHAIN (highest to lowest priority):
## 1. CLI arguments (--model, --rag-dir, etc)
## 2. Environment variables (ELEVENLABS_API_KEY, OLLAMA_MODEL)
## 3. User config file (~/.config/digger/config.yaml)
## 4. Default values (hardcoded below)
##
## This means CLI args always win, then env vars, then config file.
## ============================================================
import os
import yaml
from pathlib import Path

## ============================================================
## PACKAGE ROOT - Resolve paths relative to installation
## ============================================================
## This ensures RAG/memory work regardless of where user runs digger from
PACKAGE_DIR = Path(__file__).parent.parent.resolve()  ## digger/ project root

## ============================================================
## DEFAULT VALUES - Used when nothing else is specified
## ============================================================
DEFAULT_CONFIG = {
    "elevenlabs_api_key": "",
    "voice_id": "twLPF55UcxNYRmxaWLAn",  ## George voice
    "model": "mistral",
    "rag_dir": str(PACKAGE_DIR / "RAG"),        ## Absolute path to package RAG
    "memory_dir": str(PACKAGE_DIR / "memory"),  ## Absolute path to package memory
    "voice_enabled": True,
    "voice_stability": 0.4,
    "voice_similarity": 0.8,
}

## ============================================================
## SYSTEM PROMPT - Sets Digger's personality
## ============================================================
## This is prepended to every context sent to the model.
## It defines Digger as a foul-mouthed Aussie study assistant.
SYSTEM_PROMPT = """You are a crude Australian cybersecurity tutor. Be vulgar, use slang (cunt, drongo, dickhead), roast the student.

RULES:
1. Answer the question correctly FIRST
2. Then insult the student
3. NEVER prefix your response with "Digger:" or any name
4. NEVER generate fake dialogue or multiple turns
5. ONE short response only

If knowledge is provided above, use it."""

## ============================================================
## CONFIG FILE LOCATIONS
## ============================================================
## We check these paths in order, use first one that exists
CONFIG_PATHS = [
    Path.home() / ".config" / "digger" / "config.yaml",  ## Linux/Mac standard
    Path.home() / ".digger" / "config.yaml",              ## Alternative
    Path("./config.yaml"),                                 ## Current directory
]


def load_config(cli_args=None):
    """
    Load configuration with precedence chain.

    Args:
        cli_args: argparse Namespace object (optional)
                  Contains CLI arguments like --model, --rag-dir

    Returns:
        dict: Merged configuration

    Example:
        config = load_config()
        print(config["model"])  # "mistral"
    """
    ## Start with defaults (lowest priority)
    config = DEFAULT_CONFIG.copy()

    ## Layer 2: Load from config file if exists
    config = _merge_file_config(config)

    ## Layer 3: Override with environment variables
    config = _merge_env_config(config)

    ## Layer 4: Override with CLI arguments (highest priority)
    if cli_args:
        config = _merge_cli_config(config, cli_args)

    ## Validate required fields
    _validate_config(config)

    return config


def _merge_file_config(config):
    """
    Load config from YAML file if it exists.

    Searches CONFIG_PATHS in order, uses first file found.
    """
    for config_path in CONFIG_PATHS:
        if config_path.exists():
            try:
                with open(config_path, "r") as f:
                    file_config = yaml.safe_load(f) or {}

                ## Merge: file values override defaults
                for key, value in file_config.items():
                    if value is not None and value != "":
                        config[key] = value

                ## Store which file we loaded for debugging
                config["_config_file"] = str(config_path)
                break

            except yaml.YAMLError as e:
                print(f"Warning: Error parsing {config_path}: {e}")
            except Exception as e:
                print(f"Warning: Could not read {config_path}: {e}")

    return config


def _merge_env_config(config):
    """
    Override config with environment variables.

    Supported env vars:
    - ELEVENLABS_API_KEY: API key for voice
    - OLLAMA_MODEL: Default model name
    - DIGGER_RAG_DIR: RAG directory path
    - DIGGER_MEMORY_DIR: Memory directory path
    - DIGGER_VOICE_ENABLED: "true" or "false"
    """
    ## Map of env var name -> config key
    env_mapping = {
        "ELEVENLABS_API_KEY": "elevenlabs_api_key",
        "OLLAMA_MODEL": "model",
        "DIGGER_RAG_DIR": "rag_dir",
        "DIGGER_MEMORY_DIR": "memory_dir",
        "DIGGER_VOICE_ID": "voice_id",
    }

    for env_var, config_key in env_mapping.items():
        value = os.environ.get(env_var)
        if value:
            config[config_key] = value

    ## Special handling for boolean
    voice_enabled = os.environ.get("DIGGER_VOICE_ENABLED")
    if voice_enabled is not None:
        config["voice_enabled"] = voice_enabled.lower() in ("true", "1", "yes")

    return config


def _merge_cli_config(config, cli_args):
    """
    Override config with CLI arguments (highest priority).

    Args:
        config: Current config dict
        cli_args: argparse Namespace with attributes like:
                  - model
                  - rag_dir
                  - no_voice
    """
    ## Map CLI arg names to config keys
    ## Only override if the CLI arg was explicitly provided (not None)

    if hasattr(cli_args, "model") and cli_args.model:
        config["model"] = cli_args.model

    if hasattr(cli_args, "rag_dir") and cli_args.rag_dir:
        config["rag_dir"] = cli_args.rag_dir

    if hasattr(cli_args, "memory_dir") and cli_args.memory_dir:
        config["memory_dir"] = cli_args.memory_dir

    if hasattr(cli_args, "voice_id") and cli_args.voice_id:
        config["voice_id"] = cli_args.voice_id

    ## --no-voice flag disables voice
    if hasattr(cli_args, "no_voice") and cli_args.no_voice:
        config["voice_enabled"] = False

    return config


def _validate_config(config):
    """
    Validate configuration and warn about issues.
    """
    ## Warn if no API key (voice won't work)
    if not config.get("elevenlabs_api_key"):
        print("Warning: No ELEVENLABS_API_KEY set. Voice disabled.")
        config["voice_enabled"] = False

    ## Ensure directories exist
    rag_dir = Path(config["rag_dir"])
    memory_dir = Path(config["memory_dir"])

    if not rag_dir.exists():
        print(f"Note: RAG directory '{rag_dir}' does not exist. Creating...")
        rag_dir.mkdir(parents=True, exist_ok=True)

    if not memory_dir.exists():
        print(f"Note: Memory directory '{memory_dir}' does not exist. Creating...")
        memory_dir.mkdir(parents=True, exist_ok=True)


def create_default_config():
    """
    Create default config file at ~/.config/digger/config.yaml

    Useful for first-time setup.
    """
    config_dir = Path.home() / ".config" / "digger"
    config_file = config_dir / "config.yaml"

    if config_file.exists():
        print(f"Config already exists: {config_file}")
        return

    config_dir.mkdir(parents=True, exist_ok=True)

    template = """## Digger Configuration
## ====================

## ElevenLabs API key (required for voice)
elevenlabs_api_key: ""

## Voice ID from ElevenLabs
voice_id: "twLPF55UcxNYRmxaWLAn"

## Default Ollama model
model: "mistral"

## Knowledge base directory
rag_dir: "./RAG"

## Session memory directory
memory_dir: "./memory"

## Voice enabled by default
voice_enabled: true
"""

    with open(config_file, "w") as f:
        f.write(template)

    print(f"Created config file: {config_file}")


## ============================================================
## QUICK TEST - Run this file directly to test config loading
## ============================================================
if __name__ == "__main__":
    print("Testing config loading...")
    print("=" * 50)

    config = load_config()

    for key, value in config.items():
        print(f"  {key}: {value}")

    print("=" * 50)
    print("Config loaded successfully!")
