IMAGE_NAME = app-people-mg
FE_DEPS = build-deps
CONTAINER_NAME = app-people-mg-local
TAG ?= latest

clean:
	@echo "*** Cleaning ***"
	docker rm -f $(IMAGE_NAME) 2>/dev/null || true
	docker rmi -f $(IMAGE_NAME) 2>/dev/null || true
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi -f $(CONTAINER_NAME) 2>/dev/null || true
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf; 2>/dev/null || true

build:
	docker build \
	-t $(IMAGE_NAME):$(TAG) \
	-f Dockerfile .

run:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi -f $(CONTAINER_NAME) 2>/dev/null || true
	docker run -it -p 8003:8003 \
	--name $(CONTAINER_NAME) $(IMAGE_NAME):$(TAG)
