import connexion
from flask import jsonify, abort

from swagger_server.controllers.entities import Task
from swagger_server.db import db
from swagger_server.models import CollaboratorInner


def add_collaborator(body, task_id):  # noqa: E501
    """Add a collaborator

    Add a collaborator # noqa: E501

    :param body: Add a collaborator
    :type body: list | bytes
    :param task_id: ID of task to return
    :type task_id: int

    :rtype: Task
    """
    if connexion.request.is_json:
        body = [CollaboratorInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def add_task(body):  # noqa: E501
    """Add a task

    Add a task # noqa: E501

    :param body: Create a new task
    :type body: dict | bytes

    :rtype: Task
    """
    try:
        if connexion.request.is_json:
            d = connexion.request.get_json()
            if "task_id" in d.keys():
                d.pop("task_id")

            task = Task(**d)
            db.session.add(task)
            db.session.commit()
            return jsonify(task)
    except Exception as e:
        abort(400, str(e))




def delete_collaborator(task_id, user_id):  # noqa: E501
    """Delete a collaborator

    Delete a collaborator # noqa: E501

    :param task_id: ID of task to return
    :type task_id: int
    :param user_id: ID of collaborator to remove
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_task(task_id):  # noqa: E501
    """Deletes a task

    delete a task # noqa: E501

    :param task_id: Task id to delete
    :type task_id: int

    :rtype: None
    """
    return 'do some magic!'


def find_tasks_by_status(status=None):  # noqa: E501
    """Finds Task by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Task]
    """
    return 'do some magic!'


def get_task_by_id(task_id):  # noqa: E501
    """Find task by ID

    Returns a single task # noqa: E501

    :param task_id: ID of task to return
    :type task_id: int

    :rtype: Task
    """
    task = Task.query.filter_by(task_id=task_id).first()
    if not task:
        abort(404, f"{task_id} not found")
    return jsonify(task)


def get_task_collaborators(task_id):  # noqa: E501
    """Find task collaborators

    Returns a list of collaborators # noqa: E501

    :param task_id: ID of task to return
    :type task_id: int

    :rtype: List[User]
    """
    return 'do some magic!'


def getsub_task_by_id(task_id):  # noqa: E501
    """Find subtask list

    Returns a list of tasks # noqa: E501

    :param task_id: ID of task to return
    :type task_id: int

    :rtype: List[Task]
    """
    return 'do some magic!'


def update_task(task_id, body=None):  # noqa: E501
    """Updates a task

     # noqa: E501

    :param task_id: ID of task that needs to be updated
    :type task_id: int
    :param body: update a task
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
