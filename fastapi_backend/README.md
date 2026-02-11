# fastapi_backend

Minimal FastAPI boilerplate to confirm the backend container runs.

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Then open:

- http://localhost:8000/health
- http://localhost:8000/docs
