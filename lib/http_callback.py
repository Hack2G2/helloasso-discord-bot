#!/usr/bin/env python3
from os import getenv
from json import loads

from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

HOST = getenv("HOST")
PORT = int(getenv("PORT"))

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    req_data = loads(request.data)

    if req_data["eventType"] == "Order":
        print(req_data)

    return 'Received !'

app.run(host=HOST, port=PORT, debug=False)
