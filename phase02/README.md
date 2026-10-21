# Phase 02 — HTTP and REST

## Task 04
For `https://api.example.com/students/101`:
| Item | Value |
|---|---|
| Protocol | `https` |
| Host | `api.example.com` |
| Path | `/students/101` |
| Resource | Student |
| Resource identifier | `101` |

## Task 05
| Operation | Method | Endpoint |
|---|---|---|
| Retrieve all students | GET | `/students` |
| Create a student | POST | `/students` |
| Retrieve student 101 | GET | `/students/101` |
| Update student 101 | PUT | `/students/101` |
| Delete student 101 | DELETE | `/students/101` |

GET reads a resource, POST submits/creates, PUT updates or replaces, and DELETE requests removal.

## Tasks 06–10
Use the scripts in `phase03/api_client.py`, `phase04/api_client.py`, and `phase05/api_client.py`. Record actual responses and take screenshots. Common codes: 200 OK, 201 Created, 404 Not Found.
