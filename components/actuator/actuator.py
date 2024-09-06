from flask import Flask, request, jsonify

app = Flask(__name__)

actuator_state = {"state": "OFF"}

@app.route('/actuator', methods=['GET', 'POST'])
def actuator():
    global actuator_state
    if request.method == 'POST':
        data = request.json
        actuator_state["state"] = data.get("state", "OFF")
    return jsonify(actuator_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
