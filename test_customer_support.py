import customer_support


def setup_function():
    customer_support.requests.clear()
    customer_support.request_queue.clear()
    customer_support.action_stack.clear()


def test_add_request():
    request = customer_support.add_request(
        1, "Aisha", "Cannot log in", 2
    )
    assert request["customer"] == "Aisha"
    assert request["status"] == "Open"


def test_search_request():
    customer_support.add_request(
        2, "Musa", "Payment problem", 1
    )
    result = customer_support.search_request(2)
    assert result["customer"] == "Musa"


def test_search_missing_request():
    result = customer_support.search_request(99)
    assert result is None


def test_sort_requests():
    customer_support.add_request(
        1, "Aisha", "Login issue", 2
    )
    customer_support.add_request(
        2, "Musa", "Payment issue", 1
    )
    result = customer_support.sort_requests()
    assert result[0]["priority"] == 1
    assert result[1]["priority"] == 2


def test_queue_processes_first_request():
    customer_support.add_request(
        1, "Aisha", "Login issue", 2
    )
    customer_support.add_request(
        2, "Musa", "Payment issue", 1
    )
    result = customer_support.process_next_request()
    assert result["id"] == 1


def test_stack_returns_last_action():
    customer_support.add_request(
        1, "Aisha", "Login issue", 2
    )
    customer_support.add_request(
        2, "Musa", "Payment issue", 1
    )
    result = customer_support.get_last_action()
    assert result == "Added request 2"
