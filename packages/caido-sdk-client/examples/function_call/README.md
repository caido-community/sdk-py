# Function call example

A simple example demonstrating how to connect to a Caido instance and call a function of a plugin using the SDK.

## What it does

This example:

1. Creates a Caido client with Personal Access Token (PAT) authentication
2. Connects to the Caido instance
3. Finds the plugin (QuickSSRF)
4. Calls functions to generate an Interactsh URL

## Prerequisites

- Python 3.12+ installed
- A Caido instance running (default: `http://localhost:8080`)
- A Personal Access Token (PAT) from your Caido instance
- The QuickSSRF plugin installed on the instance

## Setup

1. Set the `CAIDO_INSTANCE_URL` environment variable (optional, defaults to `http://localhost:8080`):

   ```bash
   export CAIDO_INSTANCE_URL=http://localhost:8080
   ```

2. Set the `CAIDO_PAT` environment variable with your Personal Access Token:

   ```bash
   export CAIDO_PAT=caido_xxxxx
   ```

## Running

From the package root (`packages/caido-sdk-client`):

```bash
uv run python examples/function_call/main.py
```

Or from the repo root:

```bash
cd packages/caido-sdk-client && uv run python examples/function_call/main.py
```
