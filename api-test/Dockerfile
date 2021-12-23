FROM registry.fedoraproject.org/fedora:latest

RUN ["dnf", "upgrade", "-y"]
RUN ["dnf", "install", "-y", "openssl", "python3-devel", "libpq-devel", "gcc", "make"]
RUN ["adduser", "-m", "userman"]

#uwsgi should be built from source in prod
RUN ["sh","-c", "su userman -c 'python3 -m venv /home/userman/menv && source /home/userman/menv/bin/activate && pip install --no-cache -U pip && pip install --no-cache django uwsgi psycopg2 djangorestframework django-oauth-toolkit django-cors-headers'"]
RUN ["sh", "-c", "su userman -c 'source /home/userman/menv/bin/activate && cd /home/userman && django-admin startproject mysite && mkdir -p /home/userman/logs/django'"]

RUN ["sed", "-i", "-e","s|DEBUG = True|DEBUG = False|", "/home/userman/mysite/mysite/settings.py"]

#Insert your Domain here
RUN ["sh", "-c", "echo ALLOWED_HOSTS += [\\'127.0.0.1\\',\\'0.0.0.0\\'] >> /home/userman/mysite/mysite/settings.py"]

RUN ["dnf", "remove", "-y", "gcc", "make"]
RUN ["dnf", "clean", "all"]
COPY --chown=userman:userman uwsgi.ini /home/userman/mysite/uwsgi.ini
COPY --chown=userman:userman mysite/urls.py /home/userman/mysite/mysite/urls.py
COPY --chown=userman:userman api /home/userman/mysite/api
COPY --chown=userman:userman clockify /home/userman/mysite/clockify
COPY append.txt /mnt/dir/append.txt

COPY --chown=userman:userman activate /home/userman/menv/bin/activate
RUN cat /mnt/dir/append.txt >> /home/userman/mysite/mysite/settings.py

COPY docker-entrypoint.sh /docker-entrypoint.sh

#ENTRYPOINT ["sh","-c","su userman --preserve-environment -c 'source /home/userman/menv/bin/activate && python /home/userman/mysite/manage.py makemigrations && python /home/userman/mysite/manage.py migrate && uwsgi --ini /home/userman/mysite/uwsgi.ini'"]
ENTRYPOINT /docker-entrypoint.sh
