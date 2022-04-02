from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

@app.route('/mysqldb',methods = ['GET', 'POST'])
def display():
    if(request.method == 'POST'):
        a = request.json['db']
        b = request.json['table']
        connection = conn.connect(host='localhost', user='root', passwd='Annagem@8900')
        cur = connection.cursor()
        query = 'select * from {}.{}'.format(a,b)
        cur.execute(query)
        data = cur.fetchall()
        return jsonify(data)


if __name__ == '__main__':
    app.run()
