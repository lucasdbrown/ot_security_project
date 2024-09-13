# Actuator Dockerfile
FROM python

WORKDIR /usr/src/app

RUN apt-get update

RUN pip install flask
RUN pip install flask requests

# Copy the shell script into the container
COPY start.sh /start.sh

# Make the shell script executable
RUN chmod +x /start.sh

# Use the shell script as the entry point
CMD ["/actuator_startup.sh"]