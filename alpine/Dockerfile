FROM alpine:latest

EXPOSE 8000 8000
WORKDIR /work
RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3 py3-pip tzdata postgresql-dev gcc python3-dev musl-dev && \
    cp /usr/share/zoneinfo/Europe/Helsinki /etc/localtime && \
    echo "Europe/Helsinki" >  /etc/timezone && \
    pip install django && \
    pip install psycopg2 && \
    apk del gcc python3-dev musl-dev && \
    rm -rf /var/cache/apk/*

#python ./manage.py runserver 0.0.0.0:8000