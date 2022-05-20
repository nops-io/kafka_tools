build:
	poetry build

push: build
	poetry publish

setup:
	python3 setup.py sdist bdist_wheel
