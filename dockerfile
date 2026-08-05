# Simple Python Application
FROM python:3.8-slim

# creating a working Directory
WORKDIR /app

#copying the Dependencies file to the working directory
COPY requirements.txt .

# Installing the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the content of the files to the working directory
COPY . .

# Listening on port 5000
EXPOSE 5000

# Command to run the application
CMD [python, "app.py"]
