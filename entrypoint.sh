#!/bin/bash
set -e

if [ -n "$DJANGO_RUN_MIGRATIONS" ]; then
    python manage.py migrate --noinput
fi

if [ -n "$DJANGO_RUN_GET_MAP" ]; then
    python manage.py sde_get_map
fi

if [ -n "$DJANGO_COLLECT_STATIC" ]; then
    python manage.py collectstatic --noinput
fi

exec "$@"