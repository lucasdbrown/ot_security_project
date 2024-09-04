# SCADA

- a SCADA collects data from sensors and based on its firmware makes decisions based on that.

## SCADA described in NIST SP 800-82
"Additionally, critical infrastructures are often referred to as a “system of systems” because of the
interdependencies that exist between various industrial sectors and the interconnections between
business partners [Peerenboom][Rinaldi]. An incident in one infrastructure can directly and
indirectly affect other infrastructures through cascading and escalating failures. 

For example, both the electrical power transmission and distribution grid industries use
geographically distributed SCADA control technology to operate highly interconnected and
dynamic systems that consist of thousands of public and private utilities and rural cooperatives
for supplying electricity to end users. Some SCADA systems monitor and control electricity
distribution by collecting data from and issuing commands to geographically remote field control
stations from a centralized location. SCADA systems are also used to monitor and control water,
oil, and natural gas distribution, including pipelines, ships, trucks, rail systems, and wastewater
collection systems."

## Simulators
SCADASim: A SCADA simulator that can be installed using Python

## What is connected to a SCADA???
- Remote Terminal Units (RTUs): RTUs primarily act as the intermediaries between the field devices (like sensors and actuators) and the central SCADA system
- Programmable Logic Controllers (PLCs): PLCs communicate with the SCADA system to provide data on process variables (e.g., temperature, pressure) and to receive commands for controlling equipment.
- Human-Machine Interfaces (HMIs): HMIs are directly connected to the SCADA system, displaying process data and enabling operators to issue commands to field devices via the SCADA network.
- Sensors and Actuators: Sensors and actuators are connected to RTUs or PLCs, which then relay data to and receive commands from the SCADA system.
- Data Acquisition Systems Data acquisition systems interface with SCADA through communication protocols to transmit collected data for real-time monitoring and analysis.
- Intelligent Electronic Devices (IEDs): IEDs communicate with the SCADA system to report electrical system status, fault conditions, and to execute automated protective actions.
- Alarm Systems: Alarms are generated based on data from sensors, RTUs, and PLCs, and are managed and displayed through the SCADA system.

## How to Hack
- 
