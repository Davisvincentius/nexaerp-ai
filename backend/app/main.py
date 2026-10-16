
from fastapi import FastAPI

app = FastAPI(
    title="NexaERP AI API",
    version="0.1.0",
    description="Multi-tenant ERP with AI Assistant",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to NexaERP AI",
        "status": "running",
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "application": "NexaERP AI",
        "version": "0.1.0",
    }
