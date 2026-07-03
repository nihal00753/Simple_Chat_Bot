# Simple LangChain Chatbot (OpenRouter)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-Core-1C3C3C?style=flat-square)
![OpenRouter](https://img.shields.io/badge/API-OpenRouter%2FFree-00D084?style=flat-square)
![Status](https://img.shields.io/badge/Status-Learning%20Project-lightgrey?style=flat-square)

A minimal command-line chatbot built with LangChain, calling free open-source models through OpenRouter's Free Models Router—no local model download, no provider routing headaches, no paid API required.

This is a learning-phase project — my first hands-on practice with LangChain after struggling with HuggingFace Inference Providers. The goal was to understand the core building blocks (`ChatModel`, message types, chat history) rather than to build something production-ready.

## What it does

- Maintains a running chat history (`SystemMessage`, `HumanMessage`, `AIMessage`)
- Sends the full history to the model on every turn so it has conversational context
- Calls OpenRouter's **Free Models Router** which automatically selects from available free models
- Type `exit` to end the session

## Why OpenRouter's Free Models Router?

Instead of picking a single model that might become unavailable, use `openrouter/free` — a smart router that:
- ✅ Automatically picks the best available free model for your request
- ✅ No "model not found" errors when models change
- ✅ Works consistently with OpenAI-compatible LangChain API
- ✅ Just works — no task parameters, no provider suffixes

## Setup

1. **Get a free OpenRouter API key** (no credit card required):
   - Sign up at https://openrouter.ai
   - Go to https://openrouter.ai/keys and generate an API key
   - Copy your key

2. **Create `.env` file:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add:
   ```
   OPENROUTER_API_KEY=sk_your_key_here
   ```

3. **Install and run:**
   ```bash
   pip install -r requirements.txt
   python chatbot.py
   ```

Note: `.env` is gitignored and never uploaded — only `.env.example` (with no real key) is tracked in the repo.

## If You Want a Specific Free Model

The Free Models Router (`openrouter/free`) is recommended, but if you want a specific model, OpenRouter currently offers these free models (as of July 2026):

- `meta-llama/llama-3.3-70b:free` — General purpose, strong reasoning
- `openai/gpt-oss-20b:free` — Strong for coding tasks
- `deepseek/deepseek-r1:free` — Reasoning-heavy tasks
- `qwen/qwen-3-coder:free` — Best free coding model
- And ~25 more — see https://openrouter.ai/collections/free-models

Just change the `model=` line in chatbot.py if you want a specific one.

## What I learned

- How LangChain structures conversations as a list of typed messages
- The difference between a raw LLM wrapper and a chat-formatted model (`ChatOpenAI`)
- **HuggingFace Inference Providers is fundamentally unreliable** for most models due to provider routing
- OpenRouter's approach (unified API + auto-routing) is cleaner than managing individual providers
- Why `task="text-generation"` doesn't matter when using OpenAI-compatible APIs
- **Sometimes the best solution isn't the "obvious" one** — switching platforms was faster than debugging provider mismatches

## Troubleshooting

**"Invalid API key":**
- Make sure your `.env` has `OPENROUTER_API_KEY=sk-...` (starts with `sk-`)
- Make sure you didn't accidentally paste it into a different variable

**"No endpoints found" or "Model not found":**
- Use `model="openrouter/free"` instead of specific models — the router handles availability automatically
- If a specific model fails, the Free Models Router will pick an available one next time

**Rate limiting:**
- Free tier: 20 requests per minute (shared across all free models)
- If you hit limits, wait a minute — limits reset continuously
- For higher throughput, add $5 in credits to your OpenRouter account for unlimited access

## Next steps

- Try LangChain's prompt templates and output parsers
- Move on to Retrieval-Augmented Generation (RAG)
- Explore LangGraph for multi-step agents"# Simple_Chat_Bot" 
"# Simple_Chat_Bot" 
