# Build arguments
ARG AIRFLOW_VERSION=2.7.3
ARG PYTHON_VERSION=3.11

# Use the Airflow image with specified Python version
FROM --platform=linux/amd64 apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_VERSION}

# Set PYTHONPATH for custom DAGs
ENV PYTHONPATH="$PYTHONPATH:$AIRFLOW_HOME/dags"

# Prevent PIP reinstall packages
RUN mkdir ext

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements files into the container
COPY requirements.txt ext/requirements.txt

# Install the required packages 
RUN pip install --user --no-cache-dir -r ext/requirements.txt