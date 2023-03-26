# Description: Main application file
from fastapi import FastAPI, Body

# Create the FastAPI application
app = FastAPI()

todos = [
    {
        "created_at": "2021-01-01T00:00:00.000Z",
        "viewed": 0,
        "id": 1,
        "activity": "Learn FastAPI",
        "done": False
    },
    {
        "created_at": "2021-01-01T00:00:00.000Z",
        "viewed": 0,
        "id": 2,
        "activity": "Learn Docker",
        "done": False
    },
    {
        "created_at": "2021-01-01T00:00:00.000Z",
        "viewed": 0,
        "id": 3,
        "activity": "Learn Kubernetes",
        "done": False
    }
]

# minimal app - get request
@app.get("/", tags=["Root"])
async def root() -> dict:
    return {"ping": "pong"}

# Get --> Read Todos
@app.get("/todos", tags=["Todos"])
async def get_todos() -> dict:
    return {"data": todos}

# Post --> Create Todo
@app.post("/todos", tags=["Todos"])
async def create_todo(todo: dict = Body(...)) -> dict:  # Body(...)를 사용하여 요청 본문을 파라미터로 받습니다.
    todos.append(todo)
    return {"data": "Todo created successfully!"}

# Put --> Update Todo
@app.put("/todos/{id}", tags=["Todos"])
async def update_todo(id: int, body: dict = Body(...)) -> dict:
    for index, todo in enumerate(todos): 
        if(todo["id"] == id):
            todos[index] = body
            return {
                "data": f"Todo updated {id} successfully!"
            }
    return {
        "data": f"Todo {id} not found!"
    }


# Delete --> Delete Todo
@app.delete("/todos/{id}", tags=["Todos"])
async def delete_todo(id: int) -> dict:
    for  todo in todos: 
        if(todo["id"] == id):
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been deleted successfully!"
            }
    return {
        "data": f"Todo with id {id} wasn't found!"
    }