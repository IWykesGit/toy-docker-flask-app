# Toy Dockerized Flask App with Tests

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-%2300a3e3.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

A minimal "Hello World" Flask web app, fully Dockerized and tested with pytest. Demonstrates production basics: containerization, automated tests, and clean imports.

*Browser view at localhost:5000 + green pytest output.*

![Demo Screenshot](toy-docker-flask-app-screenshot.png)
![Pytest Screenshot](pytest-report-screenshot.png)

## Features
- Simple Flask endpoint: Returns "Docker rocks - next: SpaceX RAG! 🌌".
- Docker build/run with integrated tests (runs pytest during build).
- Pytest suite: Covers status codes, content, and emojis (Unicode-safe).
- pyproject.toml config: No import hacks - `from main import app` works everywhere.

## Quick Start

### Local Run
```bash
pip install -r requirements.txt
python main.py

Visit http://localhost:5000.
