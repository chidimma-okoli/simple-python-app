# simple-pyhton-app
FROM python:3.11-slim

# Creating the working directory
WORKDIR /app
# Adding security 
RUN useradd --create-home appuser

# Copying the dependencies
COPY requirements.txt .

# Installing the dependencies in the working Directory
RUN pip install --no-cache-dir -r requirements.txt

# Copying the other dependencies to the work directory
COPY . .

# Changing Ownership
RUN chown -R appuser:appuser /app
USER appuser

# Listening port
EXPOSE 5000

# Running the application
CMD ["python", "app.py"]
