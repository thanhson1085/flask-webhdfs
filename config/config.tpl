# Statement for enabling the development environment
DEBUG = True
APP_HOST = '192.168.1.7'
APP_PORT = 5000
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with MySQL
MYSQL_DB = "test"
MYSQL_USER = "root"
MYSQL_PORT = 3306
MYSQL_PASSWORD = "12345678"
MYSQL_HOST = "192.168.1.86"
MYSQL_CHARSET = "utf-8"

# elasticSearch Server
ELASTIC_HOST = "http://192.168.1.86"
ELASTIC_PORT = 9200
