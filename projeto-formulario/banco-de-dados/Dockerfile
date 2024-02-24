# Define a imagem base e a versão
FROM mysql:5.7

# Adiciona os scripts SQL para serem executados na criação do banco
COPY ./schema.sql /docker-entrypoint-initdb.d/

# Mapeamento da porta
EXPOSE 3306

# caminho para criar o volume nomeado
VOLUME [ "/db_data" ]

