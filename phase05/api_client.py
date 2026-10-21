import requests

BASE = "https://jsonplaceholder.typicode.com"

def explain(code):
    messages = {
        200: "OK: request succeeded.", 201: "Created: resource creation reported.",
        400: "Bad Request.", 401: "Unauthorized.", 403: "Forbidden.",
        404: "Resource not found.", 429: "Too Many Requests: rate limit may apply.",
        500: "Internal Server Error.", 502: "Bad Gateway.", 503: "Service Unavailable."
    }
    if code in messages:
        return messages[code]
    if 200 <= code < 300:
        return "Successful 2xx response."
    if 400 <= code < 500:
        return "Client error."
    if 500 <= code < 600:
        return "Server error."
    return "Unexpected status."

def test(url):
    try:
        r = requests.get(url, timeout=5)
        print(url, "| Status:", r.status_code, "|", explain(r.status_code))
        if r.status_code == 404:
            print("Request failed. Status Code: 404. Resource not found.")
    except requests.Timeout:
        print("Timeout: request exceeded 5 seconds.")
    except requests.RequestException as e:
        print("Network/request failure:", e)

def main():
    test(f"{BASE}/posts/1")
    test(f"{BASE}/posts/999999")
    print("\\nExamples of status meanings (some are illustrative, not responses generated here):")
    for c in (200, 400, 401, 404, 429, 500):
        print(c, explain(c))
    print("\\nRate limit: a cap on requests in a time window. HTTP 429 means Too Many Requests.")
    print("Loops and autonomous agents can call APIs rapidly; use sensible frequency, caching, and backoff.")

if __name__ == "__main__":
    main()
