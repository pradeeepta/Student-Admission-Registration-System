from flask import Flask, request, jsonify, render_template_string, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'college_admission'}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        connection.autocommit = True
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
