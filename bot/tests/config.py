import os

SECRET_KEY = ""

basedir = os.path.abspath(os.path.dirname(__file__))

# Database for the tests.
SQLACHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'grandpy_bot_test.db')

# Active debugger
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

