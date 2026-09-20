# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating endpoints for reading, creating, updating, and deleting task data in JSON format.

## 📝 Tasks

### 🛠️ Task 1: Set Up the FastAPI App

#### Description
Create a basic FastAPI application with a root endpoint and a small in-memory dataset for tasks.

#### Requirements
Completed program should:

- Import `FastAPI` and create an application instance
- Define a root endpoint that returns a welcome message in JSON
- Create an in-memory list of tasks to simulate a database
- Use clear endpoint names and simple JSON responses

### 🛠️ Task 2: Add Task Endpoints

#### Description
Build API routes that allow clients to retrieve all tasks and add a new task.

#### Requirements
Completed program should:

- Define a `GET /tasks` endpoint that returns the current task list
- Define a `POST /tasks` endpoint that accepts task data
- Validate required fields such as `title` and `description`
- Return the created task with a unique ID
- Use HTTP status codes that match the action taken

### 🛠️ Task 3: Add Detail, Update, and Delete Routes

#### Description
Extend the API so a client can retrieve, update, or remove a single task by ID.

#### Requirements
Completed program should:

- Define a `GET /tasks/{task_id}` endpoint for fetching one task
- Define a `PUT /tasks/{task_id}` endpoint for updating task details
- Define a `DELETE /tasks/{task_id}` endpoint for removing a task
- Return a `404` error when a task ID does not exist
- Keep the code organized and readable with clear function names

### 🛠️ Task 4: Practice JSON and Validation

#### Description
Use FastAPI features to ensure the API accepts and returns structured data predictably.

#### Requirements
Completed program should:

- Use a request model for creating or updating tasks
- Return JSON responses with consistent keys
- Store task data in a format that is easy to inspect in the browser or API client
- Include a short example of how the API can be tested using a browser or HTTP client
