import uuid

import requests


ENDPOINT = 'https://todo.pixegami.io'


def create_task(payload: dict) -> requests.Response:
    return requests.put(f'{ENDPOINT}/create-task', json=payload)


def delete_task(task_id: str) -> requests.Response:
    return requests.delete(f'{ENDPOINT}/delete-task/{task_id}')


def get_task(task_id: str) -> requests.Response:
    return requests.get(f'{ENDPOINT}/get-task/{task_id}')


def list_tasks(user_id: str) -> requests.Response:
    return requests.get(f'{ENDPOINT}/list-tasks/{user_id}')


def update_task(payload: dict) -> requests.Response:
    return requests.put(f'{ENDPOINT}/update-task', json=payload)


def new_task_payload():
    return {
        'content': f'test_content_{uuid.uuid4().hex}',
        'user_id': f'test_user_{uuid.uuid4().hex}',
        'is_done': False
    }
