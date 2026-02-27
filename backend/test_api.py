import requests
import os

def test_scan(image_path):
    url = "http://localhost:8000/scan"
    with open(image_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
        print(response.json())

if __name__ == "__main__":
    # This is a placeholder since we don't have a real image yet
    print("To test, run the FastAPI server and use the web interface or send a POST request with an image.")
