import os
import unittest
from project import app, db, ma

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
    
    # Test the main page response
    def test_main_page(self):
        response = self.app.post('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Test that items can be added
    def test_add(self):
        response = self.app.post(
          '/add/add_todo',
          data = dict(taskname="test", status = "todo"),
          follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Test that the item can be moved
    def test_move(self):
        self.test_add()
        response = self.app.get('/move/1/move_todo', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Test the response for deleting a task
    def test_delete(self):
        self.test_add()
        response = self.app.get('/move/1/delete', follow_redirects=False)
        self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()