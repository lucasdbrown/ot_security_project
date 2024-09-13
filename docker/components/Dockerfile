# Components Dockerfile
FROM python

WORKDIR /usr/src/app

RUN apt-get update

RUN pip install --no-cache-dir pymodbus==2.5.3 requests
RUN pip install requests
RUN pip install flask



# Copy the scripts to container
COPY . .

# Make the shell script executable
RUN chmod +x components_startup.sh

# Use the shell script as the entry point
CMD ["./components_startup.sh"]