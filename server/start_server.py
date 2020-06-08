from flask import Flask
from flask_restful import Api

import config
from server.request_handler import CredentialKey, ActionEndpoint, Timestamp, Sensor

app = Flask(__name__)
api = Api(app)
api.add_resource(ActionEndpoint, '/action')  # Route_1
api.add_resource(Timestamp, '/tm')  # Timestamp
api.add_resource(CredentialKey, '/credkey')
api.add_resource(Sensor, '/sensor')


def start_server():
    app.run(host='0.0.0.0', port=config.HTTP_PORT)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.HTTP_PORT)
