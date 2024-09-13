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

# Steps to Add a Modbus TCP Client in SCADA-LTS
Login to SCADA-LTS:
Access your SCADA-LTS instance through the web browser (http://localhost:8080 or the port you assigned in Docker).

## Add a New Data Source:

- Go to the Administration Panel.
- Navigate to the Data Sources section.
- Click Add New.
- Select Modbus TCP as the Data Source Type:

- In the Data Source Type, select Modbus IP from the dropdown menu.
- Server IP: Enter the IP address of your Modbus server (PLC). If it's running on the same machine as - SCADA-LTS (e.g., Docker), use localhost or the internal Docker service name (plc).
- Port: Enter 502, which is the default port for Modbus TCP communication.
- Polling Interval: Set the polling interval in milliseconds (e.g., 1000ms for 1 second).

## Configure Data Points:

- Click Add Data Point to map registers from the PLC to SCADA-LTS.
Select the Register Type:
- Holding Register (HR) for reading values like temperature from the sensor.
- Coil (C) or Discrete Input for controlling the actuator state.
- Start Address: Enter the register address (e.g., 0 for the temperature, 1 for the actuator).
- Set other fields such as Data Type (e.g., integer for temperature) and Scaling Factor if needed.

## Save the Configuration:
- After configuring the Modbus data points, save the data source.
- SCADA-LTS will start polling the PLC (Modbus TCP server) for data according to the specified interval.