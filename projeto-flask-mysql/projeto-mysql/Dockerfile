FROM mysql:latest

COPY schema.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

VOLUME ["/backup/"]
