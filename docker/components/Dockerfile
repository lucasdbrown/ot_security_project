# Components Dockerfile
FROM python

RUN apt-get update

RUN pip install --no-cache-dir pymodbus==2.5.3 requests flask

# Set the working directory
WORKDIR /usr/src/app

# Copy the scripts to container
COPY . .

# Make the shell script executable
RUN chmod +x ./components_startup.sh

# Use the shell script as the entry point
ENTRYPOINT ["./components_startup.sh"]