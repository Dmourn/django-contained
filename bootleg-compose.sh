#!/bin/bash

DB_USER='userman'
DB_NAME='userman'

if [[ ! -e  dj-db-password ]] ; then
	DB_PASSWORD="$(gpg --gen-random -a 0 32)"
	echo "${DB_PASSWORD}" > dj-db-password
else
	DB_PASSWORD="$(cat dj-db-password)"
fi

create_pod(){
	podman pod create --name=testpod -p 8080:80
}

start_nginx_and_db(){
	podman run -dt --pod=testpod --name=nginx nginx-alpine
	podman run -dt --pod=testpod --restart=always --name=db -e POSTGRES_PASSWORD="$DB_PASSWORD" \
			-e POSTGRES_USER="$DB_USER" -e POSTGRES_DB="$DB_NAME" postgres:latest
}

start_django(){
	podman run -dt --pod=testpod --restart=always --name=api -e DJ_DB_PASSWORD="{$DB_PASSWORD}" \
			-e DJ_DB_USER=$DB_USER -e DJ_DB_NAME=${DB_NAME} api-test
}

create_superuser(){
	podman exec -it --user=userman api bash \
			-c 'source /home/userman/menv/bin/activate && python /home/userman/mysite/manage.py createsuperuser'

}

create_pod
start_nginx_and_db && echo 'giving db 10 secs to start...' && sleep 10 

echo 'now django...' && start_django && sleep 5 

echo 'docker compose handles this fine, podman-compose does not' && sleep 5
create_superuser

# vi: ts=4
