
requests = []


def add_request(request_id, customer_name, issue, priority):
    request = {
        "id": request_id,
        "customer": customer_name,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    requests.append(request)
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


if __name__ == "__main__":
    add_request(1, "Aisha", "Cannot log in", 2)
    add_request(2, "Musa", "Payment problem", 1)

    print("Customer Support Requests:")
    for request in view_requests():
        print(request)
                
