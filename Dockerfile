# simple-pyhton-app
FROM python:3.11-slim

# Creating the working directory
WORKDIR /app

# Copying the dependencies
COPY requirements.txt .

# Installing the dependencies in the working Directory
RUN pip install --no-cache-dir -r requirements.txt

# Copying the other dependencies to the work directory
COPY . .

# Listening port
EXPOSE 5000

# Running the application
CMD ["python", "app.py"]
