# KPA FastAPI Backend

A backend system built with **FastAPI** and **PostgreSQL**, designed to handle submission and retrieval of detailed wheel specification form data.

## Features

- **POST** endpoint to submit wheel form data
- **GET** endpoint to retrieve wheel form data based on unique composite key (form number, submitted by, submitted date)
- Built with FastAPI and SQLAlchemy
- PostgreSQL integration
- CORS enabled for frontend compatibility
- OpenAPI(Swagger) interactive docs at `/docs`
- Example Postman collection included

## Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL 14**
- **Alembic** (migrations ready)

## Local Development (without Docker)

### Step 1: Clone the repository
```
git clone https://github.com/your-repo/kpa_fastapi_backend.git
cd kpa_fastapi_backend
```

### Step 2: Set up virtual environment and dependencies
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Add your environment config
```env
# .env
DATABASE_URL=postgresql://kpa_user:kpa_password@localhost:5432/kpa_db
```

Make sure PostgreSQL is running locally and a database named `kpa_db` is created.

### Step 4: Run the server
```
uvicorn app.main:app --reload
```

Access the API at: `http://localhost:8000`
Docs at: `http://localhost:8000/docs`

## Docker Usage (with Dockerfile only)

### Step 1: Build the Docker image
```
docker build -t kpa-fastapi-backend .
```

### Step 2: Run the Docker container
```
docker run --env-file .env -p 8000:8000 kpa-fastapi-backend
```

Make sure PostgreSQL is accessible from the container (consider using host.docker.internal for local DB access on macOS).

## API Endpoints

### POST `/formdata`
Submit a new form.

```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)"
  }
}
```

### GET `/formdata`
Query parameters:
- `formNumber`
- `submittedBy`
- `submittedDate`

Example:
```
GET /formdata?formNumber=WHEEL-2025-001&submittedBy=user_id_123&submittedDate=2025-07-03
```

## Postman Collection
Import `postman_collection.json` into Postman to test endpoints.

## Project Structure
- `app/main.py` → FastAPI app entry point
- `app/models.py` → SQLAlchemy models
- `app/schemas.py` → Pydantic schemas
- `app/database.py` → DB connection and session
- `app/routers/` → API routers for form POST and GET
- `.env` → Environment config

## Screenshots

### Uvicorn Server Up
![uvicorn_server_up(main+API)](https://github.com/vbx14/kpa_fastapi_backend/blob/4a4e29f2d6c839a9ad62677b57a834683255ad72/screenshots/uvicorn_server_up(main%2BAPI).png)

## Frontend Repo

```
git clone https://github.com/s2pl/KPA-ERP-FE.git
cd KPA-ERP-FE
```

Set this in `api_constant.dart`
```dart
const String baseUrl = 'http://localhost:8000';
```

Start Backend
```
uvicorn app.main:app --reload
```
Run the Flutter Frontend
```
flutter run -d chrome
```