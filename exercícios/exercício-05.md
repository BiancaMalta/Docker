# Exercício 05
- Criar um contêiner com nginx, com Dockerfile e index.html personalizada
- Subir um contêiner ubuntu com terminal interativo
- Colocar os dois contêineres em uma rede do tipo bridge
- Descobrir o IP atribuído ao contêiner do nginx, do contêiner do ubuntu rodar o comando: curl ip:porta
### Para isso segui os seguintes passos:
##### Criei as duas imagens solicitadas
```
docker build -t projeto-nginx .
docker build -t ubuntu .
```
##### Criei uma rede brigde
```
docker network create rede-brigde
```
##### Construi os dois containers
```
docker run -d -p 80:80 --name exercicio05-nginx --network rede-brigde projeto-nginx
docker run -it -p 82:82 --name exercicio05-ubuntu --network rede-brigde ubuntu
```
##### Inspecionei os containers 
```
docker inspect exercicio05-nginx
docker inspect exercicio05-ubuntu
```
instalar o curl via terminal ou na imagem do ubuntu
