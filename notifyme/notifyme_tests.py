import unittest
import notifyme
import json

class Test(unittest.TestCase):

    def setUp(self):
        self.app = notifyme.app.test_client()

    def test_notifications_call(self):
        response = self.app.get('/notifications/')
        self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

