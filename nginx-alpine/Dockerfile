# FROM registry.fedoraproject.org/fedora:latest
# RUN ["sh", "-c", "dnf upgrade -y && dnf install -y nginx openssl"]
FROM alpine:latest
RUN ["sh", "-c", "apk update && apk upgrade && apk add nginx openssl"]
COPY nginx.conf.uwsgi /etc/nginx/nginx.conf
COPY static /usr/share/nginx/html/static/static
ENTRYPOINT ["nginx","-g","daemon off;"]
EXPOSE 80
EXPOSE 443
