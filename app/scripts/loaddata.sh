#!/bin/bash

function load_data {
  echo "==> Removing all data from the database..."
  python manage.py flush --noinput

  echo "==> Loading owners data..."
  python manage.py loaddata sample_data/owners.json

  echo "==> Loading manufacturers data..."
  python manage.py loaddata sample_data/manufacturers.json

  echo "==> Loading cars data..."
  python manage.py loaddata sample_data/cars.json

  echo "==> Done!"
}
