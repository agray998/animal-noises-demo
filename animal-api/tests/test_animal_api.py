from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='cat')
    def test_get_animal_cat(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertIn(b'cat', response.data)
    
    @patch('application.routes.choice', return_value='dog')
    def test_get_animal_dog(self, mock_func):
        response = self.client.get(url_for('get_animal'))
        self.assert200(response)
        self.assertIn(b'dog', response.data)
        