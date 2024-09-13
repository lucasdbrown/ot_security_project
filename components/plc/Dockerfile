# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the app files
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir pymodbus requests

# Expose the Modbus TCP port
EXPOSE 502

# Run the PLC script
CMD ["python", "/app/plc.py"]
