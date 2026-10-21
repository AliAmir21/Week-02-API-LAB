# API Tool Specification

## Task 24 — Tool
- **Tool name:** `get_post`
- **Description:** Retrieve a demonstration post by ID.
- **HTTP method:** GET
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`
- **Required input:** positive integer `post_id`
- **Optional inputs:** none
- **Expected output:** JSON object with `userId`, `id`, `title`, and `body`
- **Possible errors:** 404, 429, 5xx, timeout, network failure
- **Authentication required:** no for this JSONPlaceholder endpoint

## Task 25 — Agent interface
Tool: `get_post`
Purpose: Retrieve a post using its ID.
Input: `post_id` (positive integer).
Output: `id`, `userId`, `title`, `body`.
Errors: 404 not found, 429 rate limited, 5xx server error, timeout, network failure.

An agent could call this tool when it needs post information. Validate the ID, avoid excessive repeated calls, and return clear errors. Do not expose credentials.
