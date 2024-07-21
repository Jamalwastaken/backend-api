# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CollaboratorInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, user_id: int=None):  # noqa: E501
        """CollaboratorInner - a model defined in Swagger

        :param user_id: The user_id of this CollaboratorInner.  # noqa: E501
        :type user_id: int
        """
        self.swagger_types = {
            'user_id': int
        }

        self.attribute_map = {
            'user_id': 'user_id'
        }
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt) -> 'CollaboratorInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Collaborator_inner of this CollaboratorInner.  # noqa: E501
        :rtype: CollaboratorInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> int:
        """Gets the user_id of this CollaboratorInner.


        :return: The user_id of this CollaboratorInner.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this CollaboratorInner.


        :param user_id: The user_id of this CollaboratorInner.
        :type user_id: int
        """

        self._user_id = user_id