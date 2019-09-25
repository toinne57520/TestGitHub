from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Numero(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from numero")  # This line performs query and returns json result
        print(query)
        #return {'Numero': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID

    def add(self):
        conn = db_connect.connect()
        query = con.execute("")


    def delete(self):
        conn = db_connect.connect()
        query = con.execute()

#api.add_resource(Employees, '/employees')  # Route_1
#api.add_resource(Tracks, '/tracks')  # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3

#if __name__ == '__main__':
#    app.run(port='5002')
