Python Customer Support Request System

1. Project Overview

This project is a Python-based customer support request system. It allows users to add, view, search, and sort support requests.

2. Features

- Add customer support requests.
- View all requests.
- Search requests by ID.
- Sort requests by priority.
- Automated tests using pytest.

3. Data Structures

Data Structure| Purpose
List| Stores support requests
Dictionary| Stores each request's details
Queue| Planned for processing requests in order
Stack| Planned for tracking recent actions

4. Searching and Sorting

- Searching: The program uses linear search to find a request by ID. Its time complexity is O(n).
- Sorting: The program sorts requests by priority using Python's built-in sorting. Its typical time complexity is O(n log n).

5. Testing

Automated tests are written using pytest to check adding, searching, and sorting requests.

6. Limitations

- Requests are stored in memory and are lost when the program stops.
- The program currently runs in the terminal.
- Queue and stack features still need to be implemented.

7. Future Improvements

- Implement queue and stack operations.
- Save requests to a file or database.
- Add request updates and deletion.
- Build a graphical user interface.

8. Technologies

- Python 3
- pytest

9. Project Status

Week 2 AI Engineering learning project — in development.
