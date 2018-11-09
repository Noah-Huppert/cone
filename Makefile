.PHONY: run

# run API server
run:
	gunicorn app:api
