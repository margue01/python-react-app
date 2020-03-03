IMAGE_NAME = app-people-mg
APP = $(IMAGE_NAME)-local
FE_DEPS = build-deps
CONTAINER_NAME = app-people-mg-local
TAG ?= latest

WORKSPACE_PATH  ?= $(PWD)
WORK			= /usr/src/app
RUNARGS  		= --name $(APP) --rm -w $(WORK) -v $(WORKSPACE_PATH):$(WORK)
RUNTESTS 		= pytest --cov=app-people/ --cov-report=html --cov-report xml:htmlcov/coverage.xml --disable-warnings tests

clean:
	@echo "*** Cleaning ***"
	docker rm -f $(IMAGE_NAME) 2>/dev/null || true
	docker rmi -f $(IMAGE_NAME) 2>/dev/null || true
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rm -f $(APP) 2>/dev/null || true
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf; 2>/dev/null || true

build:
	# Use Stage build to build it from BUILDER_IMAGE
	docker build \
	-t $(IMAGE_NAME):$(TAG) \
	-f Dockerfile .

# package:
	# docker build runtime image from the BUILDER_IMAGE (inherit or copying the right files from the stage build)

test: build
	# Use  BUILDER_IMAGE with test directory and no start command
	docker run $(RUNARGS) $(BUILDER_IMAGE) $(RUNTESTS)

run:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi -f $(CONTAINER_NAME) 2>/dev/null || true
	docker run -it -p 8003:8003 \
	--name $(CONTAINER_NAME) $(IMAGE_NAME):$(TAG)
