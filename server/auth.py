from datetime import datetime
import config


class Auth:

    @staticmethod
    def check(actual_token, device_id):
        if Auth.generate_token(device_id) == actual_token:
            return True
        else:
            return False

    @staticmethod
    def generate_token(device_id):
        temp = str(int(datetime.timestamp(datetime.now())))
        temp = temp[:-4]
        return Auth.sxor(Auth.sxor(config.CREDENTIAL_KEY, temp), device_id)

    @staticmethod
    def sxor(s1, s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
