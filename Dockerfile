FROM python:3-slim

# Install requirements, copy files and set workdir.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
WORKDIR ./app

# Set default env variables
ARG TELEGRAM_ID 
ENV TELEGRAM_ID=$TELEGRAM_ID

ARG TELEGRAM_HASH 
ENV TELEGRAM_HASH=$TELEGRAM_HASH

ARG TELEGRAM_TOKEN 
ENV TELEGRAM_TOKEN=$TELEGRAM_TOKEN

# Add main python command
CMD [ "python", "main.py"]