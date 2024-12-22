import requests

url = "http://localhost:8000/api/clothing-items/"
headers = {
    "Authorization": "Token def1f869482fc2231089c7d2b2da15b69850dafd"
}
data = {
    "title": "Example Title",
    "description": "Example Description",
    "size": "M"
}
files = {
    "image": open("C:\\Users\\Воронов Игорь\\Pictures\\Saved Pictures\\4An65Ed37Ac.jpg", "rb")
}

response = requests.post(url, headers=headers, data=data, files=files)

print(response.status_code)
print(response.json())
