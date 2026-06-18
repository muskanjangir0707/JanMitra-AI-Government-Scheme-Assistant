# JanMitra AI – Intelligent WhatsApp Assistant for Government Welfare Schemes

JanMitra AI is an AI-powered WhatsApp assistant designed to help citizens access information about Indian government welfare schemes. The system provides simple responses for scheme-related queries and supports basic Hindi-style interaction.

## Features

- FastAPI backend
- Government scheme PDF processing
- Basic RAG-style retrieval
- Hindi-style query support
- WhatsApp webhook support using Twilio
- Browser-based API testing using Swagger UI

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Twilio
- PyPDF
- HTML
- REST API

## Project Structure

```text
JanMitra-AI/
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
├── .gitignore
├── schemes/
│   └── pm_kisan.pdf
└── scheme_data.txt
