# Define a imagem base e a versão
FROM php:8-apache

# Copia o index.html e o cadastra-cliente.php no workdir
COPY . .

# Define o diretório principal do container
WORKDIR /var/www/html

# Atualiza a imagem com os pacotes
RUN chown -R www-data:www-data /var/www

# Mapeamento da porta
EXPOSE 80

