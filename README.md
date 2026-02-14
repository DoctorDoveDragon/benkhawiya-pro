# Benkhawiya AI - Professional Cosmic Reasoning System

A professional implementation of the Benkhawiya cosmic reasoning framework for sacredtreeofthephoenix.org.

## Overview

Benkhawiya AI is a FastAPI-based cosmic reasoning system that implements the 42 Ka Cube Principles across four council aspects:
- **SEWU**: Nurturing, Connection, Community
- **PELU**: Truth, Boundaries, Integrity
- **RUWA**: Vision, Possibility, Innovation
- **TEMU**: Structure, Proportion, Manifestation

## Features

- ✨ 42 Cosmic Principles implementation
- 🏛️ Four-aspect council decision-making system
- 📐 Golden Ratio (φ) mathematical framework
- 🌐 RESTful API with FastAPI
- 🎨 Web interface for cosmic consultations
- 🔍 Health monitoring endpoints

## Installation

### Prerequisites

- Python 3.11+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/DoctorDoveDragon/benkhawiya-pro.git
cd benkhawiya-pro

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Usage

### Run Locally

```bash
python -m uvicorn app.main:app --reload
```

Visit `http://localhost:8000` to access the web interface.

### API Endpoints

- `GET /` - Web interface
- `GET /api` - API information
- `GET /health` - Health check
- `GET /principles` - Get cosmic principles
- `POST /council/consult` - Consult the cosmic council
- `GET /mathematics/golden-ratio/{n}` - Calculate golden progression

### Example API Request

```python
import requests

response = requests.post(
    "http://localhost:8000/council/consult",
    params={"question": "How should we approach this project?"}
)
print(response.json())
```

## Development

### Code Quality

This project uses several tools to maintain code quality:

- **black**: Code formatting
- **flake8**: Linting
- **bandit**: Security scanning
- **mypy**: Type checking (optional)

### Running Quality Checks

```bash
# Format code
make format

# Run linter
make lint

# Run security scan
make security

# Run all checks
make test
```

### Manual Commands

```bash
# Format code
black app/ --line-length 127

# Lint code
flake8 app/ --max-line-length=127

# Security scan
bandit -r app/
```

## Deployment

This application is configured for deployment on:
- Railway
- Heroku
- Netlify (with functions)
- Generic cloud platforms

Environment variables:
- `PORT`: Server port (default: 8000)

## Project Structure

```
benkhawiya-pro/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── core/
│   │   ├── __init__.py
│   │   └── cosmic_engine.py # Core reasoning engine
│   ├── static/
│   │   └── favicon.ico
│   └── templates/
│       └── index.html
├── public/                  # Static assets
├── requirements.txt         # Python dependencies
├── Procfile                 # Deployment configuration
├── pyproject.toml          # Python project configuration
├── Makefile                # Development commands
└── README.md               # This file
```

## License

Copyright © 2024 Sacred Tree of the Phoenix

## Contributing

Contributions are welcome! Please ensure:
1. Code is formatted with `black`
2. All linting passes with `flake8`
3. Security scan passes with `bandit`
4. Application runs without errors

Run `make test` before submitting pull requests.

## Support

For issues and questions, please open an issue on GitHub.
