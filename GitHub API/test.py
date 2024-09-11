import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_API_URL = "https://api.github.com"
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_repository():
    url = f"{GITHUB_API_URL}/user/repos"
    data = {"name": REPO_NAME, "private": False}
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201, f"Failed to create repository: {response.json()}"
    print(f"Repository {REPO_NAME} created.")

def check_repository():
    url = f"{GITHUB_API_URL}/users/{USERNAME}/repos"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Failed to fetch repositories: {response.json()}"
    
    repos = [repo['name'] for repo in response.json()]
    assert REPO_NAME in repos, f"Repository {REPO_NAME} not found."
    print(f"Repository {REPO_NAME} is present.")

def delete_repository():
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, f"Failed to delete repository: {response.json()}"
    print(f"Repository {REPO_NAME} deleted.")

if __name__ == "__main__":
    create_repository()
    check_repository()
    delete_repository()
