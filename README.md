# FastAPI Project

A modern FastAPI application with clean architecture.

## Features

- RESTful API endpoints
- Pydantic models for data validation
- JWT authentication
- Pagination support
- Health checks
- Logging utilities

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```

## API Endpoints

- GET / - Root endpoint
- GET /items/{item_id} - Get item by ID
- POST /items/ - Create new item
- GET /health - Health check
- GET /ping - Ping endpoint

## License

MIT
