import argparse
import sys
import requests

BASE = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def get_post(post_id):
    if post_id < 1:
        print("Invalid input: post ID must be a positive integer.")
        return False

    url = f"{BASE}/posts/{post_id}"

    try:
        response = requests.get(url, timeout=TIMEOUT)

        print("Endpoint:", url)
        print("HTTP method: GET")
        print("Status:", response.status_code)

        if response.status_code == 404:
            print("Resource not found.")
            return False

        if response.status_code == 401:
            print("Authentication failed.")
            return False

        if response.status_code == 429:
            print("Rate limit reported. Slow down requests.")
            return False

        if not response.ok:
            print("API error:", response.status_code, response.text[:300])
            return False

        try:
            data = response.json()
        except ValueError:
            print("Response was not valid JSON.")
            return False

        print("User ID:", data.get("userId"))
        print("Post ID:", data.get("id"))
        print("Title:", data.get("title"))
        print("Body:", data.get("body"))

        return True

    except requests.Timeout:
        print(f"Request timed out after {TIMEOUT} seconds.")

    except requests.ConnectionError:
        print("Network failure: could not connect to API.")

    except requests.RequestException as error:
        print("Request failed:", error)

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Python JSONPlaceholder API client"
    )
    parser.add_argument("--post-id", type=int, default=1)
    args = parser.parse_args()

    return 0 if get_post(args.post_id) else 1


if __name__ == "__main__":
    sys.exit(main())