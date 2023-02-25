import traceback
from datetime import datetime, timedelta
import json
from threading import Thread, Event

from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')
