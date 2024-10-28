import os
from flask import Flask
from dotenv import load_dotenv
import mysql.connector  # Import the connector

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Load database configuration from the .env file
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_USER'] = os.getenv('DB_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')

# Function to get the database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        ssl_disabled=False  # Make sure not to disable SSL here
    )
    return connection

# Import routes
from app import routes
