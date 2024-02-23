# define a imagem base e a versão
FROM mysql:latest

# Adiciona os scripts SQL para serem executados na criação do banco
COPY ./schema.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

