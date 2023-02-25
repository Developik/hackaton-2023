import traceback
from datetime import datetime, timedelta
import json
from bson import json_util

from threading import Thread, Event

import pymongo as pymongo
from flask import Flask, request, render_template
import os

from flask_pymongo import PyMongo


from definitions import MongoDBStaticData
from utils.utils import mongodb_cmd_cases

app = Flask(__name__)

#username = os.getenv('MONGODB_USERNAME')
#password = os.getenv('MONGODB_PASSWORD')
#mongo = PyMongo(app, uri=f"mongodb+srv://{username}:{password}@cluster0.elnnjtq.mongodb.net/?retryWrites=true&w=majority")

dict_data = {

}

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/mongodb_run', methods=['POST'])
def mongodb_run():
    session = None

    print(request.method)
    if request.method == 'POST':
        print(request.args)
        cmd = request.args.get('mongo_db_command')
        cmd_id = request.args.get('cmd_id')
        static_add = MongoDBStaticData
        data = mongodb_cmd_cases(cmd, cmd_id, static_add, session)

        return (
            json.dumps(data, default=json_util.default),
            200,
            {
                'Content-Type': 'application/json',
                'Strict-Transport-Security': "max-age=31536000; includeSubDomains;"
            }
        )
