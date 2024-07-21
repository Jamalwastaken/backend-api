# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.collaborator_inner import CollaboratorInner  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTaskController(BaseTestCase):
    """TaskController integration test stubs"""

    def test_add_collaborator(self):
        """Test case for add_collaborator

        Add a collaborator
        """
        body = [CollaboratorInner()]
        response = self.client.open(
            '/api/v3/task/{taskId}/collaborator'.format(task_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_task(self):
        """Test case for add_task

        Add a task
        """
        body = Task()
        data = dict(task_id=56,
                    title='title_example',
                    description='description_example',
                    start_date='2013-10-20T19:20:30+01:00',
                    end_date='2013-10-20T19:20:30+01:00',
                    completed_at='2013-10-20T19:20:30+01:00',
                    author_id=56)
        response = self.client.open(
            '/api/v3/task',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_collaborator(self):
        """Test case for delete_collaborator

        Delete a collaborator
        """
        response = self.client.open(
            '/api/v3/task/{taskId}/collaborator/{userId}'.format(task_id=789, user_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task(self):
        """Test case for delete_task

        Deletes a task
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v3/task/{taskId}'.format(task_id=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_tasks_by_status(self):
        """Test case for find_tasks_by_status

        Finds Task by status
        """
        query_string = [('status', 'incompleted')]
        response = self.client.open(
            '/api/v3/task/findByStatus',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task_by_id(self):
        """Test case for get_task_by_id

        Find task by ID
        """
        response = self.client.open(
            '/api/v3/task/{taskId}'.format(task_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task_collaborators(self):
        """Test case for get_task_collaborators

        Find task collaborators
        """
        response = self.client.open(
            '/api/v3/task/{taskId}/collaborator'.format(task_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getsub_task_by_id(self):
        """Test case for getsub_task_by_id

        Find subtask list
        """
        response = self.client.open(
            '/api/v3/task/{taskId}/subtask'.format(task_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task(self):
        """Test case for update_task

        Updates a task
        """
        body = Task()
        response = self.client.open(
            '/api/v3/task/{taskId}'.format(task_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
