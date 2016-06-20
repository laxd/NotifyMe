class NotificationDao(object):
    def __init__(self):
        self.latest_id = 0
        self.notifications = []

    def get(self, id):
        for notification in self.notifications:
            if notification['id'] == id:
                return notification

        return None

    def create(self, source, message):
        notification = {}
        notification['id'] = self.latest_id
        notification['source'] = source
        notification['message'] = message

        self.latest_id = self.latest_id + 1

        self.notifications.append(notification)

        return notification

    def delete(self, id):
        notification = self.get(id)
        self.notifications.remove(notification)

        return notification
