#!/usr/bin/env bash

exec gunicorn app_people.wsgi:app \
              --bind 127.0.0.1:8003 \
              --timeout 600 \
              --access-logfile - \
              --error-logfile  -
