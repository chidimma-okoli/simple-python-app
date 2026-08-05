# This file start with an existing Python Enviornment
FROM python:3.12-slim

# Create a working directory folder
WORKDIR /app

# copy Dependencies into the working directory
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files into the working directory 
COPY . .

# Listen on port 5000
EXPOSE 5000

#start the container for this image
CMD ['python', 'app.py']