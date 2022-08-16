from flask import Flask
from flask import render_template
import socket
import mysql.connector
import os
import boto3
app = Flask(__name__)

DB_Host = os.environ.get('MYSQL_SERVICE_HOST') or "localhost"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "paswrd"
USER_NAME = os.environ.get('USER_NAME') or "Specify User Name"
IMAGE_URL = os.environ.get('IMAGE_URL') or "IMAGEURL"

s3 = boto3.client('s3')
s3.download_file('images-ass4', 'success.jpg', 'static/success.jpg')
s3.download_file('images-ass4', 'failed.png', 'static/failed.png')
@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password)
        color = '#39b54b'
        db_connect_result = True
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)
    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color, USER_NAME=USER_NAME, IMAGE_URL=IMAGE_URL)

@app.route("/debug")
def debug():
    color = '#2196f3'
    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set"), color=color, USER_NAME=USER_NAME, IMAGE_URL=IMAGE_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
