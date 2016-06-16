from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

sample_notifications = [
    {
        'id': 1,
        'source': u'test',
        'message': u'Testing Notifications'
    }
]


@api.route('/notifications/')
class Notification(Resource):
    def get(self):
        return sample_notifications

if __name__ == '__main__':
    app.run(debug=True)
