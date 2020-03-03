RUNARGS_LIB = --name $(APP) --rm -v $(WORKSPACE_PATH):$(WORK) -w $(WORK) --user $(UID) -e HOME=/tmp
BUILDENV  = $(RUNARGS_LIB) $(DOCKER_IMAGE):$(TAG)
TESTENV  = $(RUNARGS_LIB) $(TEST_IMAGE):$(TAG)

test-lib:
	# test image heritate from the build image, just changing config. only if necessary
	docker build -t $(TEST_IMAGE) -f docker/tester-Dockerfile .
	docker run $(TESTENV) ash -c "pip install --user -e .[dev] && pytest ./test"