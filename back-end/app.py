import traceback
from datetime import datetime, timedelta
import json
from threading import Thread, Event

import pymongo as pymongo
from flask import Flask, request, render_template
import os

from definitions import MongoDBStaticData
from utils.utils import mongodb_cmd_cases

client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.elnnjtq.mongodb.net/?retryWrites=true&w=majority")
db = client.test

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/', methods=['POST'])
def mongodb_run():
    if request.method == 'POST':
        cmd = request.form.get('mongo_db_command')
        cmd_id = request.form.get('cmd_id')
        static_add = MongoDBStaticData
        mongodb_cmd_cases(cmd, cmd_id, static_add)
