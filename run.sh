#!/bin/sh

nginx && echo "nginx started"
exec gunicorn app_people.wsgi:app \
              --bind localhost:8080 \
              --timeout 600 \
              --access-logfile - \
              --error-logfile  -
