
#from friends import Friends
#from movielists import Movielists
import flask
from flask import jsonify
from flask import request, make_response
import mysql.connector
from mysql.connector import Error
# setting up an application name
app = flask.Flask(__name__) #set up application
app.config["DEBUG"] = True #allow to show error message in browser

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET']) # default url without any routing as GET request
def home():
    return "<h1> WELCOME TO THE SHOW PAGE! </h1>"

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/api/movielist/all', methods=['GET']) #endpoint to get all the movielist
def api_movielist_all():
    return jsonify(movielist)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/api/movielist', methods=['GET']) #API to get a movielist from the db table in AWS by id as a JSON response
def api_movielist_id():
    if 'id' in request.args: #only if an id is provided as an argument, proceed
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'

    # Let make the connection to the cis3368 database on mysql
    connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")

    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM movielist"

    cursor.execute(sql)
    rows = cursor.fetchall()
    results = []

    for movielist in rows:
        if movielist['id'] == id:
            results.append(movielist)
    return jsonify(results)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Adding a friend to my database of friend
@app.route('/api/addfriend', methods=['POST'])
def addfriend():
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']


    connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")
    query = "INSERT INTO friend (firstname, lastname) VALUES ('"+firstname+"','"+lastname+"')"
    execute_query(connection, query)  
    return 'POST REQUEST ADDING FRIEND SUCCESSFUL'

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Adding a movielist to the database of movielist
@app.route('/api/addmovielist', methods=['POST'])
def addmovielist():
    request_data = request.get_json()
    friendid = request_data['friendid']
    movie1 = request_data['movie1']
    movie2 = request_data['movie2']
    movie3 = request_data['movie3']
    movie4 = request_data['movie4']
    movie5 = request_data['movie5'] 
    movie6 = request_data['movie6']
    movie7 = request_data['movie7']
    movie8 = request_data['movie8']
    movie9 = request_data['movie9']
    movie10 = request_data['movie10']

    connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")
    query = "INSERT INTO movielist (friendid, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10) VALUES ('"+friendid+"','"+movie1+"','"+movie2+"','"+movie3+"','"+movie4+"','"+movie5+"','"+movie6+"','"+movie7+"','"+movie8+"','"+movie9+"','"+movie10+"')"
    execute_query(connection, query)  
    return 'POST REQUEST ADDING MOVIELIST WORKED'


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# defined the creation of the connection to the database from inclass example
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# defined the query and read execution function from inclass example
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


app.run()