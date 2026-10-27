import requests

def get_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None
    if response.status_code != 200:
        print("Error: status", response.status_code)
        return None
    return response.json()

user = get_user("madhan007-debug")
if user:
    print(user["login"], "has", user["public_repos"], "public repos")

missing = get_user("this-user-should-not-exist-xyz-98765")
