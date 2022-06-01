install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py */*.py
lint:
	pylint --disable=R,C --ignore=static --ignore=templates */
test:
	#test not implemented
build:
	#build Docker container not implemented
deploy:
	#deploy not implemented
all: install format lint test deploy