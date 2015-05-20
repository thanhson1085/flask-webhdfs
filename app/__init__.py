from flask import Flask
import jinja2
from config import config as cfg

app = Flask(__name__)

from app.example import controllers
