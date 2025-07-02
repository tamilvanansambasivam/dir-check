import requests

# Ask for domain only (no scheme)
domain = input("Enter domain (e.g., example.com): ").strip()

# Build base URL with https
base_url = f"https://{domain}".rstrip("/")

# Ask for directory path to check
path = input("Enter directory name to check (e.g., admin): ").strip("/")

# Combine full URL
full_url = f"{base_url}/{path}"

# Send request
print("Checking:", full_url)

try:
    response = requests.get(full_url, timeout=5)
    print("Status code:", response.status_code)

    if response.status_code == 200:
        print("[FOUND] Page exists!")
    elif response.status_code == 403:
        print("[FORBIDDEN] Access denied.")
    elif response.status_code == 404:
        print("[NOT FOUND] No such directory.")
    else:
        print(f"[OTHER] Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"[ERROR] Could not reach {full_url} ({e})")
