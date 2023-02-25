import traceback
from datetime import datetime, timedelta
import json
from threading import Thread, Event

import pymongo
from flask import Flask, request, render_template, Response, stream_with_context
import os

from flask_pymongo import PyMongo
import threading

from definitions import MongoDBStaticData
from settings import db
from utils.utils import mongodb_cmd_cases, execute_command

app = Flask(__name__)
# db.init_app(app)

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

@app.route('/run-command')
def run_command():
    command = 'db.myCollection.find({})'

    # Create a new thread for the command execution
    thread = threading.Thread(target=execute_command, args=(command,))
    thread.start()

    # Return a streaming response object
    def generate():
        for line in execute_command(command):
            yield line
    response = Response(stream_with_context(generate()), mimetype='text/plain')
    return response

if __name__ == "__main__":
    app.run(debug=True)