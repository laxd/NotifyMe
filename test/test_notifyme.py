import unittest
from notifyme.notifyme import app


class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_notifications_call(self):
        response = self.app.get('/notifications/')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
