# How This PLC Works
Modbus Registers:
- Holding Registers (HR - function code 3): We use these registers to store data such as temperature and actuator states.
- Register 0 stores the temperature value (updated every 5 seconds from the sensor).
- Register 1 controls the actuator (1 for ON, 0 for OFF).
- Sensor Data: Every 5 seconds, the PLC fetches the current temperature from the sensor and updates it in Modbus register 0.
- Actuator Control: The actuator state is updated every 5 seconds by reading the value from register 1.


# Connect the PLC to SCADA-LTS
In SCADA-LTS, configure a Modbus TCP client to connect to the Modbus server running on your PLC (which is simulated using pymodbus). You'll need to:

Add a new datasource:
- Type: Modbus TCP
- Host: Set the IP address of your PLC (it will be available on localhost:502 when you run it in Docker).
Map the Modbus Registers:
- Add the corresponding Modbus registers (holding register 0 for temperature, register 1 for actuator control).