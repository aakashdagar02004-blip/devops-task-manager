from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user=os.getenv("DB_USER", "devops"),
        password=os.getenv("DB_PASSWORD", "devops123"),
        database=os.getenv("DB_NAME", "taskdb")
    )

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(tasks)

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.json

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s)",
        (data["title"],)
    )

    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Task added successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
