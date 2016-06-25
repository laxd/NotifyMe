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
        notification = {'id': self.latest_id,
                        'source': source,
                        'message': message}

        self.latest_id += 1

        self.notifications.append(notification)

        return notification

    def update(self, id, source, message):
        notification = self.get(id)

        if notification is None:
            return notification

        notification['source'] = source
        notification['message'] = message

        return notification

    def delete(self, id):
        notification = self.get(id)
        self.notifications.remove(notification)

        return notification
