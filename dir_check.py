import requests

base_url = input("Enter base URL (e.g., http://example.com): ").strip("/")
path = input("Enter directory name to check (e.g., admin): ").strip("/")

full_url = f"{base_url}/{path}"
response = requests.get(full_url)

print("Checking:", full_url)
print("Status code:", response.status_code)

if response.status_code == 200:
    print("[FOUND] Page exists!")
elif response.status_code == 403:
    print("[FORBIDDEN] Access denied.")
elif response.status_code == 404:
    print("[NOT FOUND] No such directory.")
else:
    print(f"[OTHER] Status code: {response.status_code}")
