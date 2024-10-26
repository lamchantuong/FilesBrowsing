ARG PYTHON_VERSION=3.12.7
FROM python:${PYTHON_VERSION}

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN if [ -s /tmp/requirements.txt ]; then \
    pip install -r /tmp/requirements.txt; \
    fi

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh  # Make the script executable

COPY test.py /test.py

# Set the entrypoint
ENTRYPOINT [ "/entrypoint.sh" ]
