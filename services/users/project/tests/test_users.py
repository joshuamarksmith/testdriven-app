# services/users/project/tests/test_users.py
# Tests app


import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Test user service"""

    def test_users(self):
        """Ensure the /ping route works correctly"""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
