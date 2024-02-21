# Exercício 05
- Criar um contêiner com nginx, com Dockerfile e index.html personalizada
- Subir um contêiner ubuntu com terminal interativo
- Colocar os dois contêineres em uma rede do tipo bridge
- Descobrir o IP atribuído ao contêiner do nginx, do contêiner do ubuntu rodar o comando: curl ip:porta
### Para isso segui os seguintes passos:
##### Criei os dois Dockerfile e o index.html
```
#Dockerfile ubuntu
FROM ubuntu
Run apt-get update && apt-get install -y && rm -rf /var/lib/apt/lists/* || apt update && apt upgrade \\ apt install curl
EXPOSE 80
CMD ["bash"]

#Dockerfile nginx
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80

#Arquivo index.html
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Exercício 05</title>
    <meta charset="utf-8">
  </head>
  <body>
    Arquivo solicitado.
  </body>
</html>
```
##### Criei as duas imagens solicitadas
```
docker build -t projeto-nginx .
docker build -t ubuntu .
```
##### Criei uma rede brigde
```
docker network create rede-brigde
```
##### Construi o container do nginx e descobri o IP
```
docker run -d --name exercicio05-nginx --network rede-brigde projeto-nginx
docker inspect exercicio05-nginx
```
##### Construi o container do ubuntu
```
docker run -it -p 80:80 --name exercicio05-ubuntu --network rede-brigde ubuntu
curl <ip que descobrimos>:80
```
##### Como resultado, na porta 80 vemos a imagem do nginx
