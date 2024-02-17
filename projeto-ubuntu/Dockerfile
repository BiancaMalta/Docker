# Use a imagem oficial do Ubuntu como a imagem base
FROM ubuntu:latest

# Atualize os pacotes e instale o software desejado
RUN apt-get update && apt-get install -y && rm -rf /var/lib/apt/lists/*

# Define um diretório de trabalho padrão
WORKDIR /app

# Comando padrão a ser executado quano o contêiner for iniciado
ENTRYPOINT [ "bash" ]
