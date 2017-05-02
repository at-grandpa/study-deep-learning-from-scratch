DOCKER_COMPOSE := docker-compose -f ./docker-compose.yml
DOCKER_EXEC := docker exec -it
CONTAINER_NAME := study-deep-learning-from-scratch

ps:
	$(DOCKER_COMPOSE) ps

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

clean: stop rm

stop:
	$(DOCKER_COMPOSE) stop

rm:
	$(DOCKER_COMPOSE) rm -f

attach:
	@$(DOCKER_EXEC) $(CONTAINER_NAME) /bin/bash

exec:
	@$(DOCKER_EXEC) $(CONTAINER_NAME) /bin/bash -c "$(CMD)"

jupyter:
	@$(DOCKER_EXEC) $(CONTAINER_NAME) /bin/bash -c \
		" \
		/opt/conda/bin/conda install jupyter -y --quiet && \
		mkdir /opt/notebooks && \
		/opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser \
		"
