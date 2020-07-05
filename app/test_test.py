import json
from app import get_update_visit_counter

response1 = get_update_visit_counter({}, {})
response2 = get_update_visit_counter({}, {})


def test_response():
    count1 = int(json.loads(response1["body"])["Visit_Count"])
    count2 = int(json.loads(response2["body"])["Visit_Count"])
    assert count2 - count1 == 1


def test_failure():
    assert sum([1, 2, 3]) == 7
    