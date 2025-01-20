import requests
import json

url = "http://127.0.0.1:5000/api/todos/1"
data = {
    "title": "Learn Flask",
    "description": "Study Flask and its advanced concepts",
    "completed": True
}

response = requests.put(url, json=data)
print(response.status_code)
print(response.json())