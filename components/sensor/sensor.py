from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/temperature', methods=['GET'])
def get_temperature():
    temperature = random.uniform(20.0, 30.0)  # Simulate a random temperature
    return jsonify({"temperature": temperature})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
