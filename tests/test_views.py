import unittest

import app


class IndexViewTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        app.app.testing = True  # propagate the exceptions to the test client

    def test_root_url(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/html')
        self.assertEqual(response.charset, 'utf-8')

    def test_index_url(self):
        response = self.app.get('/index')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/html')
        self.assertEqual(response.charset, 'utf-8')

    def test_help_url(self):
        response = self.app.get('/help')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/html')
        self.assertEqual(response.charset, 'utf-8')

    def test_about_url(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/html')
        self.assertEqual(response.charset, 'utf-8')


if __name__ == '__main__':
    unittest.main()
