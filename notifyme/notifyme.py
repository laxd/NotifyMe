from flask import Flask, jsonify

app = Flask(__name__)

sample_notifications = [
    {
        'id': 1,
        'source': u'test',
        'message': u'Testing Notifications'
    }
]

@app.route('/notifications/', methods=['GET'])
def get_notifications():
    return jsonify({'notifications': sample_notifications})

if __name__ == '__main__':
    app.run(debug=True)
