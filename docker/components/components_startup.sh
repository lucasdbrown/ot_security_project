#!/bin/sh

# Run the HMI, actuator, and sensor scripts
python hmi/hmi.py &
python actuator/actuator.py &
python sensor/sensor.py &

# Wait for 5 seconds to ensure the above scripts have started
sleep 5

# Run the PLC script
python plc/plc.py