import connexion
import six

from swagger_server.models.collaborator_inner import CollaboratorInner  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


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
    if connexion.request.is_json:
        body = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_task(task_id, title, description, start_date, end_date, completed_at, author_id):  # noqa: E501
    """Add a task

    Add a task # noqa: E501

    :param task_id: 
    :type task_id: int
    :param title: 
    :type title: str
    :param description: 
    :type description: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param completed_at: 
    :type completed_at: str
    :param author_id: 
    :type author_id: int

    :rtype: Task
    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    completed_at = util.deserialize_datetime(completed_at)
    return 'do some magic!'


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
    return 'do some magic!'


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
