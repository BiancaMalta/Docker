# Projeto Flask/MySQL
### Esse projeto foi desenvolvido intuito de aprender a manupilar Redes em Docker.
##### Em um primeiro momento construi a imagem de cada projeto
```
docker build -t flask-projeto .
docker build -t mysql-projeto .
```
##### Antes de subir o container, criei uma rede
```
docker network create flask-mysql
```
##### Por fim, criei o container
```
docker run -d -p 5000:5000 --name flask_conteiner --network flask-mysql flask-projeto
docker run -d -p 3306:3306 --name mysql_api_conteiner --network flask-mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql-projeto
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/cb9d5bf9-a35f-4e82-85f2-95af145f9f31)

##### Indo na extensão Thunder Client do VSC e criando uma request `GET: http://localhost:5000`, tem-se esse resultado:
<img align="center" src= "https://github.com/BiancaMalta/Docker/assets/92928037/0fe06136-24dd-46cd-ae83-1c294357ea3b"  />

##### Criando nova request `POST: http://localhost:5000/inserthost`, ele retorna apenas um nome
![image](https://github.com/BiancaMalta/Docker/assets/92928037/235b6c97-9ee8-42ff-babc-f160741fc877)

