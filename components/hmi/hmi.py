from flask import Flask, request, jsonify

app = Flask(__name__)

SENSOR_URL = 'http://sensor:5002/temperature'
ACTUATOR_URL = 'http://actuator:5001/actuator'

@app.route('/hmi', methods=['GET'])
def hmi():
    # Get sensor data
    sensor_data = requests.get(SENSOR_URL).json()
    
    # Display current actuator state
    actuator_data = requests.get(ACTUATOR_URL).json()
    
    return jsonify({
        "temperature": sensor_data['temperature'],
        "actuator": actuator_data['state']
    })

@app.route('/hmi/actuator', methods=['POST'])
def control_actuator():
    # Set actuator state (ON/OFF)
    data = request.json
    response = requests.post(ACTUATOR_URL, json=data)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)