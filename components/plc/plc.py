from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer
import logging
from threading import Thread
import time
import requests

# Configure the logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Helper function to read from sensor and update Modbus register
def update_sensor_data(context, unit=1):
    while True:
        try:
            # Fetch temperature data from sensor
            response = requests.get("http://sensor:5002/temperature")
            if response.status_code == 200:
                sensor_data = response.json()
                temperature = int(sensor_data['temperature'])  # Assuming integer values for Modbus
                # Update Modbus register (holding register) with temperature data
                context[unit].setValues(3, 0, [temperature])
                log.info(f"Updated temperature in Modbus: {temperature}")
            time.sleep(5)
        except Exception as e:
            log.error(f"Failed to update sensor data: {e}")
            time.sleep(5)

# Helper function to control actuator based on Modbus register value
def control_actuator(context, unit=1):
    while True:
        try:
            # Read actuator state from Modbus register
            actuator_state = context[unit].getValues(3, 1)[0]
            # Send the state to actuator service
            state = "ON" if actuator_state == 1 else "OFF"
            response = requests.post("http://actuator:5001/actuator", json={"state": state})
            if response.status_code == 200:
                log.info(f"Actuator set to: {state}")
            time.sleep(5)
        except Exception as e:
            log.error(f"Failed to control actuator: {e}")
            time.sleep(5)

# Function to start Modbus server
def start_modbus_server():
    # Set up data store with initial values
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*100),   # Discrete inputs
        co=ModbusSequentialDataBlock(0, [0]*100),   # Coils
        hr=ModbusSequentialDataBlock(0, [0]*100),   # Holding registers
        ir=ModbusSequentialDataBlock(0, [0]*100))   # Input registers

    context = ModbusServerContext(slaves=store, single=True)

    # Server identity
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'OT Security PLC'
    identity.ProductCode = 'PLC001'
    identity.VendorUrl = 'http://github.com'
    identity.ProductName = 'pymodbus PLC'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '1.0'

    # Start Modbus TCP Server
    log.info("Starting Modbus Server...")
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))

if __name__ == "__main__":
    # Start threads for sensor and actuator communication
    context = ModbusServerContext(slaves=ModbusSlaveContext(), single=True)
    
    sensor_thread = Thread(target=update_sensor_data, args=(context,))
    actuator_thread = Thread(target=control_actuator, args=(context,))

    sensor_thread.start()
    actuator_thread.start()

    # Start the Modbus server
    start_modbus_server()
