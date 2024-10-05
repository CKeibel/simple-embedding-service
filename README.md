# Simple Vector Service

This repository is a simple implementation of a service for embedding texts in vectors. Currently only SentenceTransfomers comatibile models are loaded by default but the code can be easily extended.
This service is provided via a simple fastapi restapi.

## Setup

Simply clone the repository, install the dependencies and start the service using python.

1. Clone repository
```
git clone
```

2. Install dependencies

via `pip`
```
python -m pip install .
```

via `poetry`
```
poetry install
```

3. Start the service
```
python main.py
```
After starting the service locally you can inspect the endpoints by visiting `http://localhost:8000/docs`.

In the future, further configuration options will follow that can be defined in `settings.toml`. In addition, api keys and other secrets can be stored in a `secrets.toml`.

## Development

This repository uses `pre-commit` hooks to ensure code qualtity. Install this git hooks via.
```
pre-commit install
```

Make sue to install `pre-commit` before.
