web: gunicorn torre.wsgi --log-file -
worker: celery -A torre worker -l info -B