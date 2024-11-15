from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 模擬資料庫 (以字典存儲資料)
fake_db = {}

# Pydantic 模型
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# 創建任務 (Create)
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    if task.id in fake_db:
        raise HTTPException(status_code=400, detail="Task already exists")
    fake_db[task.id] = task
    return task

# 讀取所有任務 (Read All)
@app.get("/tasks/", response_model=list[Task])
def read_tasks():
    return list(fake_db.values())

# 讀取單一任務 (Read One)
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return fake_db[task_id]

# 更新任務 (Update)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")
    fake_db[task_id] = task
    return task

# 刪除任務 (Delete)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in fake_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del fake_db[task_id]
    return {"message": "Task deleted successfully"}
