from flask_restplus import fields


def get_parser(api):
    parser = api.parser()
    parser.add_argument('source',
                        type=str,
                        required=True,
                        help="Notification Source",
                        location='form')
    parser.add_argument('message',
                        type=str,
                        required=True,
                        help="Notification Message",
                        location='form')


def get_model(api):
    return api.model('Notification', {
            'id': fields.Integer(required=True,
                                 description="Notification Identifier"),
            'source': fields.String(required=True,
                                    description="Notification Source"),
            'message': fields.String(required=True, description="Notification")
    })


