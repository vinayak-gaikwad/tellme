# TellMe CLI Tool

TellMe is a CLI tool to provide users with the appropriate command based on the description of what they want to do. It uses LLM with Ollama to generate commands according to user prompts.

## Requirements  
   1. Python 3.8 or higher
   2. Ollama should be running on your machine ([Ollama quickstart](https://github.com/ollama/ollama/blob/main/README.md#quickstart))


## Installation

You can install TellMe via pip:

```bash
pip install .
```
## Usage
  Type tellme followed by a clear description of your desired action.
  
[![asciicast](https://asciinema.org/a/a38IAVmKIrdrwXL3aZccA9D1C.svg)](https://asciinema.org/a/a38IAVmKIrdrwXL3aZccA9D1C)

## Configuration
TellMe uses the llama3:8b model by default. To customize this, edit the config.ini file.

### Configuration Options:
- --model: Specify the model to use (e.g., tellme --model llama3:12b).
- --config: Specify the path to a custom configuration file (defaults to config.ini).

