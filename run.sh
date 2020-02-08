#!/bin/bash

exec gunicorn app_people.wsgi:app \
              --bind 0.0.0.0:8003 \
              --timeout 600 \
              --access-logfile - \
              --error-logfile  -
