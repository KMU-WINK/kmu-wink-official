#!/bin/bash

sudo chown www-data:www-data /home/ubuntu/wink-official/db.sqlite3
sudo chown www-data:www-data /home/ubuntu/wink-official

directory="/home/ubuntu/development"

sudo python3 -m venv /home/ubuntu/wink-official/venv
source /home/ubuntu/wink-official/venv/bin/activate

sudo pip3 install --upgrade pip
sudo pip3 install -r /home/ubuntu/wink-official/requirements.txt

cp /home/ubuntu/settings.py /home/ubuntu/wink-official/settings.py

source /home/ubuntu/wink-official/venv/bin/activate
sudo python3 /home/ubuntu/wink-official/manage.py makemigrations
sudo python3 /home/ubuntu/wink-official/manage.py migrate

sudo python3 /home/ubuntu/wink-official/manage.py collectstatic --noinput
