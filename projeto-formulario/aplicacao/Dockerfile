# Define a imagem base e a versão
FROM php:8-apache

# Copia o index.html e o cadastra-cliente.php no workdir
COPY . .

# Atualiza os pacotes e instale as dependências necessárias
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libzip-dev \
    && docker-php-ext-install -j$(nproc) iconv mysqli pdo_mysql zip gd

# Define o diretório principal do container
WORKDIR /var/www/html

# Atualiza a imagem com os pacotes
RUN chown -R www-data:www-data /var/www

# Mapeamento da porta
EXPOSE 80

