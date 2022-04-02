from flask import Flask, request, jsonify
import pymongo
from pymongo import *
import json

app = Flask(__name__)

@app.route('/mongodb',methods = ['GET', 'POST'])
def display():
    if(request.method == 'POST'):
        a = request.json['connection_string']
        b = request.json['collection']
        client = pymongo.MongoClient(a)
        db = client.test
        collection = db[b]
        all_record = collection.find()
        d = {}
        for idx, record in enumerate(all_record):
            d[idx] = record

        return jsonify(str(d))


if __name__ == '__main__':
    app.run()
