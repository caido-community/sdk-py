# Upload File Example

A simple example demonstrating how to connect to a Caido instance and upload a file using the SDK.

## What it does

This example:

1. Creates a Caido client with Personal Access Token (PAT) authentication
2. Connects to the Caido instance
3. Uploads a file from the filesystem to the Caido instance
4. Displays information about the uploaded file

## Prerequisites

- Python 3.11+
- A Caido instance running (default: `http://localhost:8080`)
- A Personal Access Token (PAT) from your Caido instance

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

From the repo root, run with `uv`:

```bash
uv run --project packages/caido-sdk-client python packages/caido-sdk-client/examples/upload_file/main.py path/to/file.txt
```

You can also optionally specify a custom name for the uploaded file:

```bash
uv run --project packages/caido-sdk-client python packages/caido-sdk-client/examples/upload_file/main.py path/to/file.txt custom-name.txt
```

If no file path is provided, it will default to `test.txt` in the example directory.
