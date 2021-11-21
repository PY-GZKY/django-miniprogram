#!/bin/bash

echo "==> Removing all data from the database..."
python manage.py flush --noinput

echo "==> Loading user fixtures..."
python manage.py loaddata snippets/fixtures/users.json

echo "==> Loading snippets fixtures..."
python manage.py loaddata snippets/fixtures/snippets.json
python manage.py loaddata snippets/fixtures/entities.json

echo "==> Done!"
