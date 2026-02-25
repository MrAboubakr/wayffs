import requests
import json

# Configuration
API_BASE_URL = "https://wayffs-api.edioq.com/api/agents"
API_KEY = "YOUR_API_KEY"

headers = {
    "Authorization": f"Api-Key {API_KEY}",
    "Content-Type": "application/json"
}

def get_tasks():
    print("--- Fetching Tasks ---")
    response = requests.get(f"{API_BASE_URL}/tasks/", headers=headers)
    if response.status_code == 200:
        tasks = response.json()
        for task in tasks:
            print(f"[{task['id']}] {task['title']} - Status: {task['status']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def create_task(title, project_id, description=""):
    print(f"\n--- Creating Task: {title} ---")
    data = {
        "title": title,
        "project": project_id,
        "description": description,
        "status": "TODO"
    }
    response = requests.post(f"{API_BASE_URL}/tasks/", headers=headers, json=data)
    if response.status_code == 201:
        task = response.json()
        print(f"Success! Created task {task['id']} (shared_id: {task['shared_id']})")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # 1. List existing tasks
    get_tasks()
    
    # 2. Try creating a task (using project ID 3 from your previous test)
    # create_task("Hello from Antigravity Agent", 3, "This task was created by the AI Agent script.")
