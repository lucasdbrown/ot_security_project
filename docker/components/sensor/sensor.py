from flask import Flask, jsonify, request
import random
import time
import datetime

app = Flask(__name__)

# Global variables to simulate water temperature and sensor state
temperature = 25.0  # Initial temperature in Celsius
unit = "Celsius"  # Default unit
historical_data = []  # Store the last few readings
sensor_start_time = time.time()  # Record the sensor start time

# Configuration to simulate faults and cooling/heating events
sensor_fault = False
cooling = False
heating = False

# Helper function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Helper function to simulate temperature fluctuation over time
def simulate_temperature():
    global temperature, cooling, heating, sensor_fault
    # Simulate a slight increase or decrease in temperature based on external events
    if cooling:
        temperature -= random.uniform(0.1, 0.5)
    elif heating:
        temperature += random.uniform(0.1, 0.5)
    else:
        # Regular fluctuation (random within a small range)
        temperature += random.uniform(-0.2, 0.2)

    # Ensure temperature stays within reasonable bounds (simulate sensor limits)
    if temperature < 0 or temperature > 100:
        sensor_fault = True  # Set sensor fault if temperature goes out of bounds
    else:
        sensor_fault = False  # Reset fault if temperature is back in range

    # Add the current temperature reading to historical data (store last 10 readings)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historical_data.append({"timestamp": timestamp, "temperature": round(temperature, 2)})
    if len(historical_data) > 10:
        historical_data.pop(0)

# Route to get the current temperature, with optional simulated delay and timestamp
@app.route('/temperature', methods=['GET'])
def get_temperature():
    global temperature, unit
    simulate_temperature()  # Update temperature based on conditions

    # Simulate delay to represent data being processed by the sensor
    delay = request.args.get('delay', default=0, type=int)  # Delay in seconds
    if delay > 0:
        time.sleep(delay)  # Simulate the delay

    if sensor_fault:
        return jsonify({"error": "Sensor fault detected!"}), 500

    # Record the current timestamp for when the temperature is read
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return the temperature in the requested unit (Celsius or Fahrenheit)
    if unit == "Celsius":
        temp_reading = round(temperature, 2)
    else:
        temp_reading = round(celsius_to_fahrenheit(temperature), 2)

    return jsonify({
        "temperature": temp_reading,
        "unit": unit,
        "timestamp": timestamp,
        "delay": delay
    })

# Route to switch between Celsius and Fahrenheit
@app.route('/temperature/unit', methods=['POST'])
def switch_unit():
    global unit
    data = request.json
    if data and "unit" in data:
        if data["unit"] in ["Celsius", "Fahrenheit"]:
            unit = data["unit"]
            return jsonify({"message": f"Temperature unit set to {unit}"}), 200
        else:
            return jsonify({"error": "Invalid unit. Must be 'Celsius' or 'Fahrenheit'"}), 400
    return jsonify({"error": "No unit provided"}), 400

# Route to start or stop heating the water
@app.route('/temperature/heating', methods=['POST'])
def control_heating():
    global heating
    print(1)
    print(request.json)
    data = request.json
    print(2)
    if data and "state" in data:
        print(3)
        heating = data["state"] == "ON"
        return jsonify({"message": "Heating " + ("enabled" if heating else "disabled")}), 200
    return jsonify({"error": "Invalid request"}), 400

# Route to start or stop cooling the water
@app.route('/temperature/cooling', methods=['POST'])
def control_cooling():
    global cooling
    data = request.json
    if data and "state" in data:
        cooling = data["state"] == "ON"
        return jsonify({"message": "Cooling " + ("enabled" if cooling else "disabled")}), 200
    return jsonify({"error": "Invalid request"}), 400

# Route to retrieve the historical temperature data
@app.route('/temperature/history', methods=['GET'])
def get_history():
    return jsonify({"history": historical_data})

# Route to get sensor uptime (time since the sensor started)
@app.route('/sensor/uptime', methods=['GET'])
def get_uptime():
    uptime_seconds = time.time() - sensor_start_time
    uptime_str = str(datetime.timedelta(seconds=int(uptime_seconds)))
    return jsonify({"uptime": uptime_str})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)