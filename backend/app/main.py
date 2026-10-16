
from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine
from app.models import Company, User, CompanyMembership


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


@app.get("/api/health/database")
def database_health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "connected",
        "database": "available",
    }
