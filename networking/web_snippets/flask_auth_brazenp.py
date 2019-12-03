#Author : Roche Christopher
#File created on 30 Oct 2019 6:01 PM

from flask import Flask, request
from functools import wraps
import time

ext_app = Flask(__name__)


# Authorization method
def authorize(func):

    @wraps(func)
    def authorize_request(*args):

        #header should contain the key passcode with passcode value

        #print(request.headers)
        authcode = request.headers.get('authcode')
        if authcode != None and authcode == 'patitur':
            return func(*args)
        else:
            return unauthorised()

    return authorize_request

def isAuthcode2Authorised(authcode):

    present_time = int(time.time())

    print(present_time, authcode)
    #if authcode is the epoch value less than 10 seconds from present time
    if present_time - authcode < 10:
        return True
    else:
        return False

# Authorization method
def authorize2(func):

    def authorize2_request(*args):

        #header should contain the key passcode with passcode value

        #print(request.headers)
        authcode = request.headers.get('tempus')
        if authcode != None and isAuthcode2Authorised(int(authcode)):
            return func(*args)
        else:
            return "Failed second level authentication"

    return authorize2_request



def unauthorised():
    return "Unauthorised"

@ext_app.route('/')
@authorize
def index():
    return "The Eagle has landed"

@ext_app.route('/saturn')
@authorize
@authorize2
def saturn():
    return "Saturn is launched"

@ext_app.route('/falcon')
def falcon():
    return "LZ1: The falcon has landed"

if __name__ == '__main__':
    ext_app.run(host="0.0.0.0", port=13000)
