import os
import requests

BASE = "https://jsonplaceholder.typicode.com"

def main():
    print("JSONPlaceholder is a public demo API and does not require credentials.")
    print("API_KEY configured:", bool(os.getenv("API_KEY")))  # Do not print secret value.

    # Demonstrate header shape using a dummy token only; never use a real token here.
    headers = {"Authorization": "Bearer YOUR_DEMO_TOKEN"}
    print("Sanitized Authorization header: Bearer <REDACTED_DEMO_TOKEN>")
    assert headers["Authorization"].startswith("Bearer ")

    body = {"title": "My API Lab", "body": "Testing POST request", "userId": 1}
    for method, url, kwargs in [
        ("POST", f"{BASE}/posts", {"json": body}),
        ("PUT", f"{BASE}/posts/1", {"json": {"id": 1, **body}}),
        ("DELETE", f"{BASE}/posts/1", {}),
    ]:
        try:
            response = requests.request(method, url, timeout=10, **kwargs)
            print(f"\\n{method} {url} | Status: {response.status_code}")
            print("Response:", response.text or "(empty response body)")
        except requests.Timeout:
            print(method, "request timed out.")
        except requests.RequestException as e:
            print(method, "request failed:", e)

if __name__ == "__main__":
    main()
