# Projeto Nginx
### O objetivo desse projeto foi compreender o uso de memória no Docker, para isso, a atividade foi dividida em três parte.
1. Primeira Parte
##### Criei uma imagem 
```
docker build -t projeto-nginx .
```
##### Construi o contêiner
```
docker run -d -p 80:80 projeto-nginx
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/25558301-b894-496d-97a5-825263fea84d)
##### Editei o index.html e passei o seguinte comando
```
docker cp index.html 5ec86ad39836:/usr//share/nginx/html/
```
##### Assim, ao acessar o navegador(localhost:80), a mudança do index aparece; sendo uma praticidade para testar alterações antes de subir.
2. Segunda Parte
##### Criei um novo aquivo no container
```
docker exec -it 5ec86ad39836 bash
cd /usr/share/nginx/html
touch bianca.txt
```
<img align="right" src="https://github.com/BiancaMalta/Docker/assets/92928037/5e86aea5-31a9-47fd-96ca-4fa3d76dcdde"  width="350" height="350" />

##### Em outro terminal, eu copiei o arquivo para o meu computador, ação muito útil caso eu precise salvar algum dado do container na minha máquina.
```
docker cp 5ec86ad39836:/usr/share/nginx/html/bianca.txt .
```
##### Por fim, parei o conteiner e subi a imagem no Dockerhub
```
docker stop 5ec86ad39836
docker build -t biancamalta/nginx-projetoada:1.0.0 .
docker push biancamalta/nginx-projetoada:1.0.0
```
3. Terceira Parte
##### Subi um container com um volume nomeado mapeado
```
docker run -d -p 80:80 --name nginx-container -v volume-nginx:/var/share/nginx/html projeto-nginx
```
##### Acessei o terminal do container e criei um arquivo
```
docker exec nginx-container bash
cd /usr/share/nginx/html
echo "Bianca - aula 6" > bianca.html
exit
```
##### Compreendi que mesmo matando e emovendo o container, o volume continua 
```
docker stop nginx-container
docker rm nginx-container
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/1d80cea2-3ddf-4f2a-a456-e4dda68e4955)
##### E ao subir outro container com esse volume, o conteúdo criado se mantém
##### Para terminar, removi o volume
```
docker volume rm volume-nginx
```
### Os arquivos que estão nesse diretório e não foram utilizados nos passos acima, são resultado do [exercício 03](https://github.com/BiancaMalta/Docker/blob/main/exerc%C3%ADcios/exerc%C3%ADcio-03.md)



