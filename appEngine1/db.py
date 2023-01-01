import os
import pymqsl
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        # Una variable del servidor del cloud
        # Si app.yaml existe, agarra los datos
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymqsl.connect(user=db_user,password=db_password,
                                unix_socket=unix_socket, db=db_name, cursorclass=pymysql.cursors.DictCursor)

    except pymysql.MySQLError as e:
        print(e)
        return e
    return conn

def get_users():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM users;')
        users = cursor.fetchall()
        if result > 0:
            got_users = jsonify(users)
        else:
            got_users = 'no hay usuarios en la bd'
    conn.close()
    return got_users

def add_user(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO users(user_name, user_email, user_password) VALUES (%s,%s,%s)',
                        (user["nombre"],user["email"],user["password"]))
    conn.commit()
    conn.close
