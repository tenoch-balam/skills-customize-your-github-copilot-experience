# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a RESTful API using FastAPI that handles HTTP requests and returns JSON responses. You'll learn to build endpoints, validate request data, and implement proper error handling.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Build a FastAPI application with GET and POST endpoints that handle different HTTP methods. Start with a simple in-memory data store to manage resources.

#### Requirements
Completed program should:

- Define a Pydantic model for request/response data validation
- Implement at least one GET endpoint that returns all items
- Implement at least one POST endpoint that creates a new item
- Use proper HTTP status codes (200, 201, 404, etc.)
- Run on `localhost:8000` and be accessible via curl or REST client


### 🛠️ Add Request Validation and Error Handling

#### Description
Enhance your API to properly validate incoming requests and provide meaningful error responses when something goes wrong.

#### Requirements
Completed program should:

- Validate request body fields using Pydantic models
- Return 400 Bad Request for invalid data with helpful error messages
- Return 404 Not Found for requests to non-existent resources
- Add path parameters to endpoints (e.g., `/items/{id}`)
- Implement DELETE and/or PUT methods for updating or removing items


### 🛠️ Advanced: Add Database Persistence (Stretch Goal)

#### Description
Extend your API to store data in a database instead of relying on in-memory storage, making your API persistent across restarts.

#### Requirements
Completed program should:

- Use SQLAlchemy with SQLite or another database of choice
- Persist data across API restarts
- Maintain all previous endpoint functionality
- Document your API endpoints (FastAPI auto-generates Swagger docs at `/docs`)
