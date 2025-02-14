#!/usr/bin/env bash
# start-server.sh
/etc/init.d/cron start

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd face_website; python manage.py createsuperuser --no-input)
fi
(cd face_website; gunicorn face_website.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"
