import connexion
from flask import jsonify, abort

from swagger_server.controllers.entities import Task, Subtask
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
    delete_count = Task.query.filter_by(task_id=task_id).delete()
    db.session.commit()
    if delete_count == 0:
        abort(404, f"{task_id} not found")


def find_tasks_by_status(status=None):  # noqa: E501
    """Finds Task by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Task]
    """
    if status == "incompleted":
        tasks = Task.query.filter(Task.completed_at.is_(None)).all()
    elif status == "completed":
        tasks = Task.query.filter(Task.completed_at.isnot(None)).all()
    else:
        abort(400, "invalid status value")
    return jsonify(tasks)


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
    tasks = Subtask.query.filter(Subtask.parent_task_id == task_id).all()
    return jsonify(tasks)

def add_subtask(task_id, body):  # noqa: E501
    """Find subtask list

    Returns a list of tasks # noqa: E501

    :param task_id: ID of task to return
    :type task_id: int

    :rtype: List[Task]
    """
    response = add_task(body)
    child_id = response.json.get('task_id')
    subtask = Subtask(parent_task_id=task_id, child_task_id=child_id)
    db.session.add(subtask)
    db.session.commit()

def delete_subtask(task_id, subtask_id):
    delete_count = Subtask.query.filter(
        Subtask.parent_task_id == task_id,
        Subtask.child_task_id == subtask_id,
    ).delete()
    db.session.commit()
    if delete_count == 0:
        abort(404, "No subtasks found")
    else:
        _ = Task.query.filter(Task.task_id == task_id).delete()
        db.session.commit()

def update_task(task_id, body=None):  # noqa: E501
    """Updates a task

     # noqa: E501

    :param task_id: ID of task that needs to be updated
    :type task_id: int
    :param body: update a task
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            d = connexion.request.get_json()
            if "task_id" in d.keys():
                d.pop("task_id")

            task = Task.query.filter_by(task_id=task_id).first()
            if task:
                for key, value in d.items():
                    setattr(task, key, value)
                db.session.add(task)
                db.session.commit()
                return jsonify(task)
    except Exception as e:
        abort(400, str(e))

    abort(404, f"{task_id} not found")

