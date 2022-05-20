FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN ["apt", "update"]
RUN ["apt", "upgrade", "-y"]
RUN ["apt", "install", "-y", "bash", "util-linux", "libssl-dev", "openssl", "python3-venv", "python3-dev", "libpq-dev", "gcc", "make", "postgresql"]
RUN ["useradd", "-m", "userman", "-s", "/bin/bash"]

#uwsgi should be built from source in prod
RUN ["bash","-c", "su userman -s /bin/bash -c 'python3 -m venv /home/userman/menv && source /home/userman/menv/bin/activate && pip install --no-cache -U pip && pip install --no-cache django uwsgi psycopg2 djangorestframework django-oauth-toolkit django-cors-headers'"]
RUN ["bash", "-c", "su userman -s /bin/bash -c 'source /home/userman/menv/bin/activate && cd /home/userman && django-admin startproject mysite && mkdir -p /home/userman/logs/django'"]

RUN ["sed", "-i", "-e","s|DEBUG = True|DEBUG = False|", "/home/userman/mysite/mysite/settings.py"]

#Insert your Domain here
RUN ["bash", "-c", "echo ALLOWED_HOSTS += [\\'127.0.0.1\\',\\'0.0.0.0\\'] >> /home/userman/mysite/mysite/settings.py"]

RUN ["apt", "remove", "-y", "gcc", "make"]
RUN ["apt-get", "clean"]
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
