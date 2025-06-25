import requests

url = "http://example.com/admin"  # hardcoded for now
response = requests.get(url)

print("Status code:", response.status_code)
