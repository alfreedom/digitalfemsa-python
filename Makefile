python-test:
	pytest

clean:
	rm -rf ./dist

python:
	rm -rf docs && \
	rm -rf digitalfemsa/models && \
	docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli:v7.14.0 generate \
	-i https://raw.githubusercontent.com/digitaltitransversal/openapi/refs/heads/main/_build/api.yaml \
	-g python \
	-o /local \
	-c /local/config-python.json \
	--global-property modelTests=false
