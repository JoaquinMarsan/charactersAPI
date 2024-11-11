# Character API

## Introduction

A RESTful API built with FastAPI, SQLAlchemy, and SQLite that allows users to interact with character data.

## Features

- Retrieve all characters (/getAll)
- Retrieve a character by ID (/get/{id})
- Add a new character (/add)
- Delete a character by ID (/delete/{id})

## Requirements

- Python 3.7+
- SQLite
- Docker (optional)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/JoaquinMarsan/charactersAPI.git
   cd character-api
2. **Create a virtual environment**
    ```bash
    conda create -n pythonchallange python=3.8
    conda activate pythonchallange
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Run the application**
    ```bash
    uvicorn app.main:app --reload
Use another port if default (8000) is in use

4. **Access the API documentation**
    - OpenAPI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc

## Docker Deployment

1. **Build the Docker image**
    ```bash
    docker build -t character-api .
2. **Build the Docker image**
    ```bash
    docker run -d -p 80:80 character-api
The API will be accessible at http://localhost
