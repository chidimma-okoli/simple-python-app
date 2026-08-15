from flask import Flask, jsonify, request
from tasks import get_all_tasks, add_task, complete_task
import time
import mysql.connector
import os

app = Flask(__name__)

for attempt in range(10):
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("Connected to MySQL successfully!")
        break
    except mysql.connector.Error as err:
        print(f"MySQL not ready yet: {err}")
        time.sleep(3)
else:
    raise RuntimeError("Could not connect to MySQL after several attempts")

@app.route("/")
def home():
    return {
        "message": "Welcome to my Docker Task Manager API"
    }

@app.route("/tasks", methods=["GET"])
def tasks():
    return jsonify(get_all_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "Title is required"}, 400

    task = add_task(data["title"])

    return jsonify(task), 201

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):

    task = complete_task(id)

    if task:
        return jsonify(task)

    return {"error": "Task not found"}, 404

@app.route("/users")
def users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from users")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)