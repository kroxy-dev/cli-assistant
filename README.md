# CLI AI Assistant
A command-line AI assistant with persistent conversation memory, powered by the Groq API.

## What it does
- Chat with an AI directly in your terminal
- Conversation history is saved between sessions — the assistant remembers previous conversations
- Gracefully handles API errors without crashing

## Requirements
- Python 3.13+
- `requests` and `python-dotenv` libraries

## Installation
1. Clone the repo:
```
git clone https://github.com/kroxy-dev/cli-assistant.git
```
2. Install dependencies:
```
pip install requests python-dotenv
```
3. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_key_here
```
Get a free key at [console.groq.com](https://console.groq.com).

## Usage
```
python groq.py
```

## Model
Uses `llama-3.1-8b-instant` via the Groq API. Can be swapped for any other Groq-supported model by changing the model name in `groq.py`.
