# Building Components with Flask in Python

# Installation

## Installing Flask
`pip install Flask`

## Install Flask requests
`pip install flask requests`

## Install pymodbus (inside components folder)
`pip install pymodbus`

## Instructions to start curling
- will have 4 terminals
- cd into the individual components and run the following `python <component>.py`
- then you can curl in the one non-component terminal by cding into components

# Using the components

## Getting the temperature

### Retrieving data from `curl`
`curl http://127.0.0.1:5002/temperature`

## Temperature history
`curl http://127.0.0.1:5002/temperature/history`

## Change the unit of temperature
`curl -X POST -H "Content-Type: application/json" -d '{"unit": "Fahrenheit"}' http://127.0.0.1:5002/temperature/unit`

## Enabling heating
`curl -X POST -H "Content-Type: application/json" -d '{"state": "ON"}' http://127.0.0.1:5002/temperature/heating`

## Disabling heating
`curl -X POST http://127.0.0.1:5002/temperature/heating -H "Content-Type: application/json" -d '{"state": "OFF"}'`

## Enabling cooling
`curl -X POST -H "Content-Type: application/json" -d '{"state": "ON"}' http://127.0.0.1:5002/temperature/cooling`

## Disabling cooling
`curl -X POST http://127.0.0.1:5002/temperature/cooling -H "Content-Type: application/json" -d '{"state": "OFF"}'`

## See the uptime of the sensor
`curl http://127.0.0.1:5002/sensor/uptime`

## Controlling the actuator with HMI
### Turning it on
`curl -X POST -H "Content-Type: application/json" -d '{"state": "ON"}' http://127.0.0.1:5000/actuator`
`curl -X POST http://127.0.0.1:5001/actuator -H "Content-Type: application/json" -d '{"state": "ON"}'`

### Turning it off
`curl -X POST -H "Content-Type: application/json" -d '{"state": "OFF"}' http://127.0.0.1:5000/actuator`
`curl -X POST http://127.0.0.1:5001/actuator -H "Content-Type: application/json" -d '{"state": "OFF"}'`

## Actuator test
`curl http://127.0.0.1:5001/actuator`

