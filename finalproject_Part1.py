#from friends import Friends
#import movielists
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
    

    # Let make the connection to the cis3368 database on mysql
    connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")

    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM movielist"

    cursor.execute(sql)
    movielist = cursor.fetchall()
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

    for movie in rows:
        if movie['id'] == id:
            results.append(movie)
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

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Update the friend from friends table
@app.route('/api/updatefriend', methods=['PUT'])  # using put method to UPDATE
def update_friend():
    request_data = request.get_json()
    friendid = request_data['friendid']
    firstname = request_data['firstname']
    lastname = request_data['lastname']

    # establishing the connection
    if firstname and lastname and friendid and request.method == "PUT":

        connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")
        update_query = "UPDATE friend SET firstname = '%s', lastname = '%s' WHERE friendid = %s" % (firstname, lastname, friendid)
        execute_query(connection, update_query)
        return 'PUT REQUEST UPDATED FRIEND SUCCESSFUL'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Update the movielist from movielist table
@app.route('/api/updatemovielist', methods=['PUT'])  # using put method to UPDATE
def update_movielist():
    request_data = request.get_json()
    #id = request_data['id']
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

    # establishing the connection
    if movie1 and movie2 and movie3 and movie4 and movie5 and movie6 and movie7 and movie8 and movie9 and movie10 and friendid and request.method == "PUT":

        connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")
        update_query = "UPDATE movielist SET movie1 = '%s', movie2 = '%s', movie3 = '%s', movie4 = '%s', movie5 = '%s', movie6 = '%s', movie7 = '%s', movie8 = '%s', movie9 = '%s', movie10 = '%s' WHERE friendid = %s" % (movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, friendid)
        execute_query(connection, update_query)
        return 'PUT REQUEST UPDATED MOVIELIST SUCCESSFUL'


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Delete a friend from the database of friend
@app.route('/api/deletefriend', methods=['DELETE'])  # using delete method to delete
def deletefriend():
    request_data = request.get_json()
    friendid = request_data['friendid']

    # establishing the connection
    connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")
    # deleting from the friends table where where id is = friendid
    delete_query = "DELETE FROM friend WHERE friendid = %s" % (friendid)
    execute_query(connection, delete_query)
    delete_movielist_query = "DELETE FROM movielist WHERE friendid = '%s'" % (friendid)
    execute_query(connection, delete_movielist_query)
    return 'DELETE REQUEST DELETING FRIEND SUCCESSFUL'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ramdom Selection of movie from the database of movielist
@app.route('/api/random', methods=['GET'])
def random():
    
    # Let make the connection to the cis3368 database on mysql
    connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")
    #query_random = "SELECT * FROM movielist ORDER BY RAND() LIMIT 1;"
    #execute_query(connection, query_random)

    cursor = connection.cursor(dictionary=True)
    sql = "SELECT movie5 FROM movielist ORDER BY RAND() LIMIT 1;"
    cursor.execute(sql)
    movielist = cursor.fetchall()
    return jsonify(movielist)

    

    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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