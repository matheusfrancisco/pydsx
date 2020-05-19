PHONY: \
	__build_python_test_image \
	test_python_data_structures \
  lint_python

__build_python_test_image:
	cd python-data-structure && \
    docker build -f .docker/test.Dockerfile -t data-structure-test .


test_python_data_structures:
	cd python-data-structure && \
    make test

lint_python:
	cd python-data-structure && \
    make lint
