requests = []
request_queue = []
action_stack = []


def add_request(request_id, customer_name, issue, priority):
    request = {
        "id": request_id,
        "customer": customer_name,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    requests.append(request)
    request_queue.append(request)
    action_stack.append(f"Added request {request_id}")
    return request


def view_requests():
    return requests


def search_request(request_id):
    for request in requests:
        if request["id"] == request_id:
            return request
    return None


def sort_requests():
    return sorted(requests, key=lambda request: request["priority"])


def process_next_request():
    if request_queue:
        return request_queue.pop(0)
    return None


def get_last_action():
    if action_stack:
        return action_stack.pop()
    return None


if __name__ == "__main__":
    add_request(1, "Aisha", "Cannot log in", 2)
    add_request(2, "Musa", "Payment problem", 1)

    print("All Support Requests:")
    for request in view_requests():
        print(request)

    print("\nNext Request in Queue:")
    print(process_next_request())

    print("\nLast Action in Stack:")
    print(get_last_action())
