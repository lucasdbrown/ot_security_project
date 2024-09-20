# Operational Technology (OT) Security Project
## Project Overview
This project simulates a cyber attack on an industrial complex's infrastructure by creating a containerized environment with a SCADA, PLC, and connected components that resemble and simulate the functions of an industrial water plant. We researched relevant CVEs that have been found in industrial complexes, later specializing in finding exploits applicable to SCADAs. We used Docker for containerizing our environment and implemented SCADA-LTS as our simulated SCADA. We simulated components that would be connected to a SCADA in an industrial water plant environment by using Flask in python to simulate the functions and operations of the components and how they send data. These components send their data first to the Programmable Logical Controller (PLC) and then get transmitted to the SCADA by the Modbus protocol which we simulated by using the pymodbus library in our python file for the PLC.


## Diagram of our simulated Water Plant
<img src="https://github.com/user-attachments/assets/a7b53266-32c2-4a01-952d-653ddf027b7a" width="500" height="700">

#### Programmable Logical Controller (PLC)
- we used the `pymodbus` library to simulate the functions of a real PLC

#### Human Machine Interface (HMI)
- used Flask in Python to simulate the functions of an HMI to control the functions of the sensor and actuator

#### Water Sensor
- simulated the functions of a water sensor using Flask in Python

#### Actuator
- simulated the functions of an actuator using Flask in Python

## How to Setup?
- Install docker desktop (if not already)
- In the directory with the `docker-compose.yml`
- `docker-compose up`

#### To connnect to the terminal
- `docker ps` for the name or id of the scadalts container
- `docker exec -it <container_name/id> /bin/bash` to connect to shell

#### To view the different webpages
- [Scada](http://localhost:8080/Scada-LTS/)
  - username: admin
  - password: admin
- [HiveMQ](http://localhost:8081/)
  - username: admin
  - password: hivemq
