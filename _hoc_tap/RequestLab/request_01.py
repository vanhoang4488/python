import requests

r = requests.get("http://github.com")
print(r.json)
