from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        "nombre":"Enrique",
        "email":"jose.medranod@udem.edu",
        "password":"666"
    },
    {
        "nombre":"Felipe",
        "email":"felipe.medrano@udem.edu",
        "password":"666"
    },
    {
        "nombre":"Roberto",
        "email":"roberto.medrano@udem.edu",
        "password":"666"
    }
]

@app.route('/')
def display():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_users():
    user = request.get_json()
    users.append(user)
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)