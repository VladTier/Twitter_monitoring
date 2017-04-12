import unittest

from app.views import app


class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up correctly
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True)
        self.assertIn(b'You were just logged in', response.data)

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='bla', password='bla'),
            follow_redirects=True)
        self.assertIn(b'Invalid credentials.Please try again', response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were just logged out', response.data)


if __name__ == '__main__':
    unittest.main()
