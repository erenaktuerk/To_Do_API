import requests

url = "http://127.0.0.1:5000/api/todos/"
data = {"title": "Learn Flask", "description": "Study the basics of Flask"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.text)