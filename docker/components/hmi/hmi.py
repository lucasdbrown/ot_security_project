from flask import Flask, jsonify, request
import requests
import logging

app = Flask(__name__)

# Sensor service URLs
SENSOR_URL = 'http://127.0.0.1:5002/temperature'
HISTORY_URL = 'http://127.0.0.1:5002/temperature/history'
UNIT_URL = 'http://127.0.0.1:5002/temperature/unit'
HEATING_URL = 'http://127.0.0.1:5002/temperature/heating'
COOLING_URL = 'http://127.0.0.1:5002/temperature/cooling'
UPTIME_URL = 'http://127.0.0.1:5002/sensor/uptime'

# Actuator service URL
ACTUATOR_URL = 'http://127.0.0.1:5001/actuator'

# Set up logging
logging.basicConfig(level=logging.DEBUG)

### SENSOR CONTROL ROUTES ###

# 1. Get the current temperature (supports delay)
@app.route('/hmi/temperature', methods=['GET'])
def get_temperature():
    delay = request.args.get('delay', default=0, type=int)  # Optional delay parameter
    try:
        response = requests.get(f"{SENSOR_URL}?delay={delay}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to sensor service: {e}")
        return jsonify({"error": "Failed to connect to sensor service", "details": str(e)}), 500

# 2. Switch between Celsius and Fahrenheit
@app.route('/hmi/temperature/unit', methods=['POST'])
def switch_unit():
    data = request.json
    try:
        response = requests.post(UNIT_URL, json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to sensor service: {e}")
        return jsonify({"error": "Failed to connect to sensor service", "details": str(e)}), 500

# 3. Start or stop heating the water
@app.route('/hmi/heating', methods=['POST'])
def control_heating():
    data = request.json
    try:
        response = requests.post(HEATING_URL, json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to sensor service: {e}")
        return jsonify({"error": "Failed to connect to sensor service", "details": str(e)}), 500

# 4. Start or stop cooling the water
@app.route('/hmi/cooling', methods=['POST'])
def control_cooling():
    data = request.json
    try:
        response = requests.post(COOLING_URL, json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to sensor service: {e}")
        return jsonify({"error": "Failed to connect to sensor service", "details": str(e)}), 500

# 5. Retrieve historical temperature data
@app.route('/hmi/temperature/history', methods=['GET'])
def get_history():
    try:
        response = requests.get(HISTORY_URL)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to sensor service: {e}")
        return jsonify({"error": "Failed to connect to sensor service", "details": str(e)}), 500

# 6. Get the uptime of the sensor
@app.route('/hmi/uptime', methods=['GET'])
def get_uptime():
    try:
        response = requests.get(UPTIME_URL)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to sensor service: {e}")
        return jsonify({"error": "Failed to connect to sensor service", "details": str(e)}), 500

### ACTUATOR CONTROL ROUTES ###

# 7. Control the actuator (turn ON/OFF)
@app.route('/hmi/actuator', methods=['POST'])
def control_actuator():
    try:
        # Extract the state (ON/OFF) from the incoming request
        data = request.json
        logging.debug(f"Received actuator control command: {data}")
        
        # Send the state to the actuator service
        response = requests.post(ACTUATOR_URL, json=data)
        logging.debug(f"Actuator service responded with: {response.text}")
        
        # Return the response from the actuator service
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to actuator service: {e}")
        return jsonify({"error": "Failed to connect to actuator service", "details": str(e)}), 500
    except Exception as e:
        logging.error(f"An internal error occurred: {e}")
        return jsonify({"error": "An internal error occurred", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=open)
