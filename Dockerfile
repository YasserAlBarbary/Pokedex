# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /Pokedex

# Install dependencies
COPY Pipfile Pipfile.lock /Pokedex/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /Pokedex/