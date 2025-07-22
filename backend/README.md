# TimeFlow Backend

This is the Python backend for the TimeFlow time-accounting MVP.

## Getting Started

1. (Recommended) Create and activate a virtual environment.
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn sqlalchemy
   ```
3. Run the development server:
   ```sh
   uvicorn main:app --reload
   ```

---

## Project Structure
- `/main.py` — FastAPI entrypoint
- `/models.py` — SQLAlchemy models
- `/db/` — Database schema/migrations

---

For frontend setup, see the `../frontend` folder.
