from unittest import TestCase
from notifyme.dao import NotificationDao


class TestNotificationDao(TestCase):
    def setUp(self):
        self.dao = NotificationDao()

        # Add some test data
        self.dao.notifications.append({"id": 99,
                                       "source": "test",
                                       "message": "test message"})

    def test_get(self):
        result = self.dao.get(99)
        self.assertEquals("test", result['source'])

    def test_create(self):
        self.dao.create("test create", "test message")

        result = self.dao.get(0)
        self.assertEquals("test create", result['source'])

    def test_update(self):
        result = self.dao.update(99, "test updated", "test message")

        self.assertEqual("test updated", result['source'])

    def test_delete(self):
        result = self.dao.delete(99)

        self.assertNotIn(result, self.dao.notifications)
