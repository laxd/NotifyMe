from flask import Flask
from flask_socketio import SocketIO
from flask_restplus import Api, Resource
from .dao import NotificationDao
from .swagger import get_parser, get_model

app = Flask(__name__)
api = Api(app)
dao = NotificationDao()
socketio = SocketIO(app)

dao.create("Test Source", "Test Message")

parser = get_parser(api)
model = get_model(api)


@api.route('/notifications/')
class NotificationList(Resource):
    def get(self):
        return dao.notifications

    @api.doc(parser=parser)
    @api.marshal_with(model)
    def post(self):
        args = parser.parse_args()
        print("Got args: %s" % args)
        return dao.create(args['source'], args['message'])


@api.route('/notifications/<int:id>')
class Notification(Resource):
    def get(self, id):
        notification = dao.get(id)

        if notification is None:
            api.abort(404, "Notification {} doesn't exist".format(id))

        return notification

    def post(self):
        args = parser.parse_args()

        return dao.update(args['id'], args['source'], args['message'])

    def delete(self, id):
        return dao.delete(id)


@socketio.on("notification")
def deliver_notification(notification, source):
    dao.create(source, notification)
    print("received notification '%s' from '%s'" % (notification, source))
