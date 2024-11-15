import requests

BASE_URL = "http://127.0.0.1:8000/tasks/"

# 創建任務
task = {"id": 1, "title": "Learn FastAPI", "completed": False}
response = requests.post(BASE_URL, json=task)
print("Create Task:", response.json())

# 讀取所有任務
response = requests.get(BASE_URL)
print("Read All Tasks:", response.json())

# 讀取單一任務
response = requests.get(f"{BASE_URL}1")
print("Read One Task:", response.json())

# 更新任務
updated_task = {"id": 1, "title": "Learn FastAPI - Updated", "completed": True}
response = requests.put(f"{BASE_URL}1", json=updated_task)
print("Update Task:", response.json())

# 刪除任務
response = requests.delete(f"{BASE_URL}1")
print("Delete Task:", response.json())
