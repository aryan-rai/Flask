from flask import flask, jsonify, request
app = Flask(__name__)

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status";"error",
            "message": "Please provide data"
        }, 400)

"data" : [
    {
        "Contact": "9987644456",
        "Name" : "Raju",
        "done" : false,
        "id": 1
    },
    {
        "Contact": "9876543222",
        "Name" : "Rahul",
        "done" : false,
        "id" : 2
    }
]
tasks = {
    'id' : tasks[-1]['id'] + 1
    'Name' : request.json['Name'],
    'Contact' : request.json.get('Contact', "")
    'done' : False
}
tasks.append(task)
return jsonify({
    "status": "success"
    "message" : "Task added successfully"
})