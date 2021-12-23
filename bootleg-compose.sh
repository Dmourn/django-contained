#!/bin/bash

DB_PASSWORD="$(gpg --gen-random -a 0 32)"
DB_USER='userman'
DB_NAME='userman'

echo "Password is ${DB_PASSWORD}"

if [[ -z $(which docker 2>/dev/null) && -n $(which podman) ]]; then
	echo 'yes podman';
	podman pod create --name=testpod -p 8080:80
	podman run -dt --pod=testpod --name=nginx nginx-base
	podman run -dt --pod=testpod --restart=always --name=db -e POSTGRES_PASSWORD="$DB_PASSWORD" -e POSTGRES_USER="$DB_USER" -e POSTGRES_DB="$DB_NAME" postgres:latest \
	&& echo 'giving db 10 secs to start ...' && sleep 10 
	podman run -dt --pod=testpod --restart=always --name=api -e DJ_DB_PASSWORD="{$DB_PASSSWORD}" -e DJ_DB_USER=$DB_USER -e DJ_DB_NAME=${DB_NAME} api-test
	echo 'now django...'
	sleep 5 
	echo 'docker compose handles this fine, not podman-compose though'
	sleep 5
	podman exec -it --user=userman api bash -c 'source /home/userman/menv/bin/activate && python /home/userman/mysite/manage.py createsuperuser'
fi	

if [[ -n $(which docker 2>/dev/null) && -z $(which podman) ]]; then
	echo 'try changing podman to docker in the script. I need to write a docker-compose';
fi
