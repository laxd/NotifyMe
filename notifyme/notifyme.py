from flask import Flask
from flask_restplus import Api, Resource
from .dao import NotificationDao
from .swagger import get_parser, get_model

app = Flask(__name__)
api = Api(app)
dao = NotificationDao()
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

    def delete(self, id):
        return dao.delete(id)

if __name__ == '__main__':
    app.run(debug=True)
