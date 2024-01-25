install:
	poetry install

start:
	export http_proxy='http://185.217.143.125:80'
	poetry run python main.py
