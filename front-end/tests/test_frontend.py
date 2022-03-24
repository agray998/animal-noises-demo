from application import app, db
from application.models import Results
from flask import url_for
import requests_mock
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app
    
    def setUp(self):
        sample_result = Results(animal='cat', noise='meow')
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal-api:5000/get-animal', json={"animal":"dog"})
            m.post('http://noise-api:5000/noise', json={"noise":"woof"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'cat goes meow', response.data)
            self.assertIn(b'dog goes woof', response.data)
