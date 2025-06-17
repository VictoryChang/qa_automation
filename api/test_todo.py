from icecream import ic
import requests

from api.todo import ENDPOINT, new_task_payload, create_task, delete_task, get_task, list_tasks, update_task


def test_can_call_endpoint():
    # health check
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # get the task and verify content
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']


def test_can_update_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # update the task
    new_payload = {
        'user_id': payload['user_id'],
        'content': 'new content',
        'is_done': True,
        'task_id': task_id
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get the task and verify content
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']


def test_can_list_tasks():
    # create N number of tasks
    n = 3
    payload = new_task_payload()
    for i in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # list the tasks for user_id
    user_id = payload['user_id']
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    tasks = list_task_response.json()['tasks']
    assert len(tasks) == n


def test_can_delete_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # delete the task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # get the task and verify it does not exist
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
