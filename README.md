# CodeVector Backend

FastAPI + PostgreSQL backend for CodeVector app.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt

Create .env file in root folder:
DATABASE_URL=postgresql://postgres.kunblxgnobtaadisirae:`your_password_here`@db.kunblxgnobtaadisirae.supabase.co:5432/postgres

Seed database:
python -m app.seed

Start server:
uvicorn app.main:app --reload
Server will run on http://localhost:8000
Docs: http://localhost:8000/docs