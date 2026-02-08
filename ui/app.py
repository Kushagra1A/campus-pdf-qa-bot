import requests

BACKEND_URL = "http://localhost:8000"

print("Campus PDF Q&A UI")

try:
    response = requests.get(f"{BACKEND_URL}/health")
    print("Backend response:", response.json())
except Exception as e:
    print("Could not connect to backend:", e)
