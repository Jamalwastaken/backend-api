import connexion
import six

from swagger_server.controllers.entities import User
from swagger_server.db import db
#from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(body=None):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        #body = User.from_dict(connexion.request.get_json())  # noqa: E501
        d = connexion.request.get_json()
        email = d.get("email")
        password = d.get("password")
        username = d.get("username")
        _create_user(username, email, password)

    return 'do some magic!'


def _create_user(username=None, email=None, password=None):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param user_id: 
    :type user_id: int
    :param username: 
    :type username: str
    :param email: 
    :type email: str
    :param password: 
    :type password: str

    :rtype: User
    """
    user = User(email=email, password=password, username=username)
    db.session.add(user)
    db.session.commit()
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def login_user(username=None, password=None):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_user(username, body=None):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be deleted
    :type username: str
    :param body: Update an existent user in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user(username, user_id=None, username2=None, email=None, password=None):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be deleted
    :type username: str
    :param user_id: 
    :type user_id: int
    :param username2: 
    :type username2: str
    :param email: 
    :type email: str
    :param password: 
    :type password: str

    :rtype: None
    """
    return 'do some magic!'
