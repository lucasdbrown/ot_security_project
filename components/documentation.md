# Building Components with Flask in Python

# Installation

## Installing Flask
`pip install Flask`

## Install Flask requests
`pip install flask requests`

# Using the components

## Getting the temperature

### Retrieving data from `curl`
`curl http://127.0.0.1:5000/temperature`

## Controlling the actuator with HMI
### Turning it on
`curl -X POST -H "Content-Type: application/json" -d '{"state": "ON"}' http://127.0.0.1:5000/hmi/actuator`

### Turning it off
`curl -X POST -H "Content-Type: application/json" -d '{"state": "OFF"}' http://127.0.0.1:5000/hmi/actuator`



