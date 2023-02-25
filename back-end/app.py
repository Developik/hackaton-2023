import traceback
from datetime import datetime, timedelta
import json
from threading import Thread, Event

import pymongo as pymongo
from flask import Flask, request, render_template
import os

from flask_pymongo import PyMongo


from definitions import MongoDBStaticData
from settings import db
from utils.utils import mongodb_cmd_cases

#db =

app = Flask(__name__)
#db.init_app(app)

username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
mongo = PyMongo(app, uri=f"mongodb+srv://{username}:{password}@cluster0.elnnjtq.mongodb.net/?retryWrites=true&w=majority")

dict_data = {

}

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/', methods=['POST'])
def mongodb_run():
    session = None
    if request.method == 'POST':
        cmd = request.form.get('mongo_db_command')
        cmd_id = request.form.get('cmd_id')
        static_add = MongoDBStaticData
        mongodb_cmd_cases(cmd, cmd_id, static_add, session)
