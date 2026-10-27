import json
import requests

username = input("GitHub username: ")
response = requests.get(f"https://api.github.com/users/{username}", timeout=10)

if response.status_code == 200:
    data = response.json()
    summary = {
        "login": data["login"],
        "public_repos": data["public_repos"],
        "followers": data["followers"],
    }
    with open("profile.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Saved profile.json")
else:
    print("Not found, status", response.status_code)
