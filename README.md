# Python Customer Support Request System

## Project Overview
This project is a Python-based customer support request system. It allows users to add, view, search, and sort customer support requests.

## Features
- Add customer support requests.
- View all support requests.
- Search for requests by ID.
- Sort requests by priority.
- Process requests using a queue (FIFO).
- Track recent actions using a stack (LIFO).
- Automated tests using pytest.
- Automated testing with GitHub Actions.

## Data Structures

| Data Structure | Purpose |
|---|---|
| List | Stores support requests |
| Dictionary | Stores each request's details |
| Queue | Processes requests in first-in, first-out order |
| Stack | Tracks actions in last-in, first-out order |

## Searching and Sorting

- Searching: Linear search by request ID, with time complexity O(n).
- Sorting: Sorts requests by priority, typically O(n log n).

## Queue and Stack

- Queue: `process_next_request()` processes the earliest queued request.
- Stack: `get_last_action()` returns and removes the most recent action.

## Testing
Automated tests use pytest to check adding, searching, sorting, queue processing, and stack actions.

GitHub Actions automatically runs the tests when changes are pushed to the main branch or a pull request targets main.

## Limitations
- Requests are stored in memory and are lost when the program stops.
- The program currently runs in the terminal.
- Request updates and deletion are not yet implemented.

## Future Improvements
- Save requests to a file or database.
- Add request updates and deletion.
- Build a graphical user interface.

## Technologies
- Python 3.11
- pytest
- GitHub Actions

## Project Status
Week 2 AI Engineering learning project.
