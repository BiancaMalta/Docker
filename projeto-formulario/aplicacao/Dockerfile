# define a imagem base e a versão
FROM php:8.2-cli

# Define o diretório principal do container
WORKDIR /var/www/html/

# Copia o index.html e o process.php no workdir
COPY . .

# Atualiza a imagem com os pacotes
RUN chown -R www-data:www-data /var/www

# Mapeamento da porta
EXPOSE 5000

