# CLI AI Assistant

A command-line AI assistant with persistent conversation memory, powered by the Groq API.

## What it does

- Chat with an AI directly in your terminal
- Conversation history is saved between sessions — the assistant remembers previous conversations
- Gracefully handles API errors without crashing

## Requirements

- Python 3.13+
- `requests` library

## Installation

1. Clone the repo:
```
git clone https://github.com/kroxy-dev/cli-assistant.git
```

2. Install dependencies:
```
pip install requests
```

## Usage

```
python cli.py
```

You will be prompted to enter your Groq API key. Get a free key at [console.groq.com](https://console.groq.com).

## Model

Uses `llama-3.1-8b-instant` via the Groq API. Can be swapped for any other Groq-supported model by changing the model name in `groq.py`.
