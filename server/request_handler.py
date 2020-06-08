from time import sleep

from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse
from flask import jsonify
from datetime import datetime
import config
from server import auth
from telegram_bot.command_hendler import *
from telegram_bot.bot_start import logger

next_action = {}
parser = reqparse.RequestParser()
parser.add_argument('lamps_status')
first_boot = True


class ActionEndpoint(Resource):
    @staticmethod
    def get():
        headers = request.headers
        dev_id = headers.get('D-ID')
        if auth.Auth.check(headers.get('X-Auth'), dev_id) or config.NOT_NEED_AUTH:
            result = {'action': 'nop'}
            if rooms_temp != rooms_temp_prev:
                result = {'temp': rooms_temp.get(dev_id)}
                if result.get('temp') is None:
                    print(result.get('temp'))
                    return abort(404)
                rooms_temp_prev.update(rooms_temp)

        else:
            logger.error('not valid auth token')
            return abort(404)

        return jsonify(result)


class Sensor(Resource):
    @staticmethod
    def post():
        current_temp = request.get_json(force=True).get('temp')
        d_id = request.get_json(force=True).get('temp')
        rooms_current_temp.update({d_id: current_temp})


class Timestamp(Resource):
    @staticmethod
    def get():
        return str(int(datetime.timestamp(datetime.now())))[:-4]


class CredentialKey(Resource):
    @staticmethod
    def get():
        return config.CREDENTIAL_KEY
