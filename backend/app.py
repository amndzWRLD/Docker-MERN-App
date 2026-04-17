from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

def get_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="app_db"
            )
            return conn
        except:
            print("Waiting for DB...")
            time.sleep(2)

@app.route("/list")
def list_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos")
    result = cursor.fetchall()
    return jsonify(result)

@app.route("/")
def home():
    return "API RUNNING"

app.run(host="0.0.0.0", port=5000)
