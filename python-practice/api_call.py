import requests

response = requests.get("https://api.github.com/users/madhan007-debug")
print(response.status_code)

data = response.json()
print(data["login"])
print(data["public_repos"])
print(data["html_url"])
