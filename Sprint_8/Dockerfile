# Use an official Python runtime as a parent image
FROM python:3.9

# Define the working directory within the container
WORKDIR /app

# Copy the local script to the container
COPY seu_script.py /app/

# Install the required Python libraries
RUN pip install requests pandas

# Run the Python script
CMD [ "python", "ex1.py" ]
