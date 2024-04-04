FROM python:3.11

ARG PACKAGE_NAME

# Set the working directory in the container
WORKDIR /app

# Copy test dependencies
COPY requirements-test.txt .
COPY pytest.ini .

# Install any needed packages specified in requirements-test.txt
RUN pip install --no-cache-dir -r requirements-test.txt
