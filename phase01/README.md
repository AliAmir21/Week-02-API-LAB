# Phase 01 — Browser and Client/Server

## Task 01
Open and screenshot:
- https://jsonplaceholder.typicode.com/posts/1
- https://jsonplaceholder.typicode.com/posts/2
- https://jsonplaceholder.typicode.com/posts/3

Record the actual `userId`, `id`, `title`, and `body` values from each response. Changing the ID requests a different post, so the returned resource changes.

## Task 02
```text
Browser (client) -- HTTP GET /posts/1 --> API endpoint --> Server/data
Browser (client) <-- JSON HTTP response -- API endpoint <-- Server/data
```
The browser sends a request to `/posts/1`. The API routes it to the server-side application, which finds the requested post and returns JSON. The browser displays that response. The browser uses the API contract without needing to know the server's internal implementation.

## Task 03
| Endpoint | Resource | Specific resource? |
|---|---|---|
| `/posts` | Collection of posts | No |
| `/posts/1` | Post with ID 1 | Yes |
| `/posts/2` | Post with ID 2 | Yes |
