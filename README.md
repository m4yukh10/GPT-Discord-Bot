# Discord GPT & Quote Bot

This Discord bot is designed to perform two main functions: provide inspirational quotes and respond to user messages using OpenAI's GPT-3.5 Turbo model. It's built using the `discord.py` library for interaction with Discord and the `openai` Python client for generating text responses.

## Features

- **Inspirational Quotes**: Upon receiving a specific command (e.g., "inspire kor amay"), the bot fetches a random inspirational quote from ZenQuotes.io and sends it in the chat.
- **GPT-3.5 Turbo Interaction**: For other messages, the bot uses OpenAI's GPT-3.5 Turbo model to generate and send a relevant response based on the user's input.

## Prerequisites

Before you can run this bot, you'll need to install the following:
- Python 3.6 or higher
- `discord.py` library
- `requests` library
- `openai` Python client

Additionally, you must have a Discord bot token and an OpenAI API key.

