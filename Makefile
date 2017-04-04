REPOSITORY=deep
TAG=default

HOST_WORKDIR=$(PWD)
CONTAINER_WORKDIR=/root/deep

build:
	docker build --tag=$(REPOSITORY):$(TAG) .

attach:
	docker run -v $(HOST_WORKDIR):$(CONTAINER_WORKDIR) -it $(REPOSITORY):$(TAG)

