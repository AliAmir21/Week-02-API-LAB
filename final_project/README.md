# Final Integration Project — API Client

## Endpoint
`GET https://jsonplaceholder.typicode.com/posts/{post_id}`

## Input and response
Required input: positive integer `post_id`. GET has no request body. Expected JSON fields are `userId`, `id`, `title`, and `body`.

## Run
From the `API-Lab` root:
```bash
python -m pip install -r final_project/requirements.txt
python final_project/src/api_client.py
python final_project/src/api_client.py --post-id 2
python final_project/src/api_client.py --post-id 999999
```

## Error handling
Checks HTTP status, handles 404 and other unsuccessful responses, uses a 10-second timeout, and handles network errors. The Phase 05 script demonstrates messages for common status codes, including 400, 401, 429 and 500.

## Authentication
The selected JSONPlaceholder endpoint is public and does not need an API key. For protected APIs, load credentials from environment variables; never hardcode or commit secrets.

## Agent tool
This function could later be exposed as `get_post(post_id)`. The agent supplies a validated ID and receives the returned fields or a clear error.
