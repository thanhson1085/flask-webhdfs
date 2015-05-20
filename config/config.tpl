# Statement for enabling the development environment
DEBUG = True
APP_HOST = '192.168.1.191'
APP_PORT = 5000
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_ROOT = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))
TEMPLATE_ROOT = os.path.join(BASE_ROOT, 'templates/')
STATIC_ROOT = os.path.join(BASE_ROOT, 'static/')


# logs
# log level:
#   0: all log (this is default)
#   10: debug, info, warning, error log
#   20: info, warning, error log
#   30: warning, error log
#   40: only error log
#   50: nothing
LOG_LEVEL = 0
LOG_FILE = 'logs/application.log'
