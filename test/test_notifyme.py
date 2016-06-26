from unittest import TestCase
from notifyme import notifyme


class TestApiCalls(TestCase):
    def setUp(self):
        self.app = notifyme.app.test_client()

        notifyme.dao.create("source", "message")

    def test_notifications_call(self):
        response = self.app.get('/notifications/')
        self.assertEquals(response.status_code, 200)

    def test_notifications_present(self):
        response = self.app.get('/notifications/1')
        self.assertEquals(response.status_code, 200)
        pass

    def test_notifications_missing(self):
        response = self.app.get('/notifications/3')
        self.assertEquals(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
