#!/bin/sh

sh -c "su userman --preserve-environment -c 'source /home/userman/menv/bin/activate && python /home/userman/mysite/manage.py makemigrations \
	&& python /home/userman/mysite/manage.py migrate && uwsgi --ini /home/userman/mysite/uwsgi.ini'"
