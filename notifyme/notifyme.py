from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

sample_notifications = [
    {
        'id': 1,
        'source': u'test',
        'message': u'Testing Notifications'
    },
    {
        'id': 2,
        'source':u'test2',
        'message': u'ITS WORKING!'
    }
]


@api.route('/notifications/')
class NotificationList(Resource):
    def get(self):
        return sample_notifications
    
@api.route('/notifications/<int:id>')
class Notification(Resource):
    def get(self, id):
        for notification in sample_notifications:
            if notification['id'] == id:
                return notification

        api.abort(404, "Notification {} doesn't exist".format(id))


if __name__ == '__main__':
    app.run(debug=True)
