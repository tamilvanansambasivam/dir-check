import requests

base_url = input("Enter base URL (e.g., http://example.com): ").strip("/")
path = input("Enter directory name to check (e.g., admin): ").strip("/")

full_url = f"{base_url}/{path}"
response = requests.get(full_url)

print("Checking:", full_url)
print("Status code:", response.status_code)
