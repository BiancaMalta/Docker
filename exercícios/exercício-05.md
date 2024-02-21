# Exercício 05
- Criar um contêiner com nginx, com Dockerfile e index.html personalizada
- Subir um contêiner ubuntu com terminal interativo
- Colocar os dois contêineres em uma rede do tipo bridge
- Descobrir o IP atribuído ao contêiner do nginx, do contêiner do ubuntu rodar o comando: curl ip:porta
### Para isso segui os seguintes passos:
##### Criei os dois Dockerfile e o index.html
###### Caso não coloque a instalar do pacote curl no Dockerfile do ubuntu, será necessário instala-lo via terminal `apt-get update` `apt install curl`

##### Criei as duas imagens solicitadas
```
docker build -t nginx05 .
docker build -t ubuntu05 .
```
##### Criei uma rede brigde
```
docker network create rede-brigde
```
##### Construi o container do nginx e descobri o IP
```
docker run -d --name exercicio05-nginx --network rede-brigde nginx05
docker inspect exercicio05-nginx
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/11cc3803-ef89-431b-ad02-c381e26491d6)

##### Construi o container do ubuntu
```
docker run -it -p 80:80 --name exercicio05-ubuntu --network rede-brigde ubuntu05
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/9638e351-2ff0-4203-afc2-088cb01106c4)
##### E executei o comando exigido `curl <ip encontrado>: 80`. Como resultado, o terminal retornou a imagem do nginx
![image](https://github.com/BiancaMalta/Docker/assets/92928037/5c6234d6-01f2-404e-8a4c-e95c064a51ea)

##### Para mais detalhes, deixei os arquivos que gerados pela atividade nessa [pasta](https://github.com/BiancaMalta/Docker/tree/main/exerc%C3%ADcios/exerc%C3%ADcio-05)

