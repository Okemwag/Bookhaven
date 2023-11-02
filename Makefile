# Makefile for Dockerized Django Application

# Environment variables
ENV_FILE := .env

# Docker commands
DOCKER_COMPOSE := docker-compose
DOCKER_EXEC := $(DOCKER_COMPOSE) exec web
DOCKER_RUN := $(DOCKER_COMPOSE) run --rm web

# Docker Compose configuration
COMPOSE_FILE := docker-compose.yml

# Django management commands
MANAGE := $(DOCKER_EXEC) python manage.py
MANAGE_NO_DOCKER := python manage.py

# Development server configuration
PORT := 8000
HOST := 0.0.0.0

.PHONY: build up down stop restart logs migrate createsuperuser

# Build the Docker containers
build:
	$(DOCKER_COMPOSE) build

# Start the Docker containers in the background
up:
	$(DOCKER_COMPOSE) up -d

# Stop the Docker containers
down:
	$(DOCKER_COMPOSE) down

# Stop the Docker containers gracefully
stop:
	$(DOCKER_COMPOSE) stop

# Restart the Docker containers
restart: down up

# View the logs of the running containers
logs:
	$(DOCKER_COMPOSE) logs -f

# Make migrations
makemigrations:
	$(MANAGE) makemigrations

# Apply database migrations
migrate:
	$(MANAGE) migrate

# Create a superuser for Django admin
createsuperuser:
	$(MANAGE) createsuperuser

# Collect static files
collectstatic:
	$(MANAGE) collectstatic --noinput

# Run Django development server
runserver:
	$(MANAGE) runserver $(HOST):$(PORT)

# Access Django shell
shell:
	$(MANAGE) shell

# Run tests
test:
	$(MANAGE) test

# Run the linting checks
lint:
	$(DOCKER_RUN) flake8 .

# Open a shell in the web container
bash:
	$(DOCKER_EXEC) bash

# Open a shell in the database container
dbbash:
	$(DOCKER_EXEC) db bash

# Open a shell in the redis container
redisbash:
	$(DOCKER_EXEC) redis bash

# Show this help message
help:
	@echo "Available commands:"
	@echo "  make build              - Build the Docker containers"
	@echo "  make up                 - Start the Docker containers in the background"
	@echo "  make down               - Stop the Docker containers"
	@echo "  make stop               - Stop the Docker containers gracefully"
	@echo "  make restart            - Restart the Docker containers"
	@echo "  make logs               - View the logs of the running containers"
	@echo "  make migrate            - Apply database migrations"
	@echo "  make createsuperuser    - Create a superuser for Django admin"
	@echo "  make collectstatic      - Collect static files"
	@echo "  make runserver          - Run Django development server"
	@echo "  make shell              - Access Django shell"
	@echo "  make test               - Run tests"
	@echo "  make lint               - Run linting checks"
	@echo "  make bash               - Open a shell in the web container"
	@echo "  make dbbash             - Open a shell in the database container"
	@echo "  make redisbash          - Open a shell in the redis container"
	@echo "  make help               - Show this help message"

# Include environment variables from .env file
ifneq ($(wildcard $(ENV_FILE)),)
	include $(ENV_FILE)
	export
endif
