from flask import Flask, jsonify, request
import requests
import logging

app = Flask(__name__)

ACTUATOR_URL = 'http://127.0.0.1:5001/actuator'

@app.route('/hmi/actuator', methods=['POST'])
def control_actuator():
    try:
        # Extract the state (ON/OFF) from the incoming request
        data = request.json
        logging.debug(f"Received actuator control command: {data}")
        
        # Send the state to the actuator service
        response = requests.post(ACTUATOR_URL, json=data)
        
        # Return the response from the actuator service
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to actuator service: {e}")
        return jsonify({"error": "Failed to connect to actuator service"}), 500
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=open)
