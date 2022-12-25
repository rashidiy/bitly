all:
	docker start rashideveloper
	docker start infallible_northcutt
	celery -A apps worker --beat