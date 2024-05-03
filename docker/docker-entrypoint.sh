#!/bin/sh
python manage.py showmigrations | grep "\[ \]"
if [ $? -eq 0 ]; then
    python manage.py migrate --no-input
fi
exec "$@"
