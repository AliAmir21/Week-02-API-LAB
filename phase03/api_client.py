import requests

BASE = "https://jsonplaceholder.typicode.com"

def show_post(post_id):
    try:
        r = requests.get(f"{BASE}/posts/{post_id}", timeout=10)
        print(f"\\nGET /posts/{post_id} | Status: {r.status_code}")
        if r.status_code == 200:
            post = r.json()
            print("Post ID:", post.get("id"))
            print("Title:", post.get("title"))
            print("Body:", post.get("body"))
        else:
            print("Response:", r.text)
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as e:
        print("Request failed:", e)

def main():
    # Task 11: JSON object represented as a Python dictionary.
    student = {"name": "Ali", "marks": 85, "program": "BSCS"}
    print(student["name"], student["marks"], student["program"])

    # Task 12: JSON array represented as a list of dictionaries.
    students = [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Sara"}, {"id": 3, "name": "Ahmed"}]
    for s in students:
        print("Student ID:", s["id"], "Name:", s["name"])

    # Tasks 13–14: reuse one function to retrieve three records.
    for post_id in (1, 2, 3):
        show_post(post_id)

    # Task 15: retrieve collection, count records, print five titles.
    try:
        r = requests.get(f"{BASE}/posts", timeout=10)
        print("\\nGET /posts | Status:", r.status_code)
        r.raise_for_status()
        posts = r.json()
        print("Number of posts:", len(posts))
        for post in posts[:5]:
            print("-", post.get("title"))
    except requests.Timeout:
        print("Collection request timed out.")
    except requests.RequestException as e:
        print("Could not retrieve posts:", e)

if __name__ == "__main__":
    main()
