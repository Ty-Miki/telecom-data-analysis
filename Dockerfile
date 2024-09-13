# Use an official Python runtime as a parent image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /model

# Copy the current directory contents into the container at /model
COPY . /model/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 avaliable to the outside world
EXPOSE 80

# Run the regression script when the container launches
CMD [ "python", "./model/app.py" ]