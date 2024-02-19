# Exercício 03
- Suba um contêiner com a imagem do nginx
- Crie um volume do tipo bind
- Mapeie a pasta que está a salvo seu arquivo index.html
- Após subir o contêiner, edite o arquivo e veja a mudança ocorrendo

### Para isso, executei os seguintes comandos:
##### Entrei dentro da pasta do projeto nginx e criei uma nova pasta para o volume bind 
```
cd projeto-nginx
mkdir volume-bind
```
##### Executei o build da imagem
```
docker build -t projeto-nginx .
```
##### Subi o container com a imagem e o volume requisitado
```
docker run -d -p 80:80 --name exercicio03 -v ./volume-bind/:/usr/share/nginx/html/volume-bind projeto-nginx
```
##### Mapiei a pasta
```
docker inspect exercicio3
```
##### Editei o arquivo
```
docker exec -it exercicio03 bash
cd /usr/share/nginx/html/
echo "arquivo editado" > index.html
echo "novo arquivo" > bianca.html
```
##### Parei/matei o container e notei que o conteúdo criado e alterado se manteve salvo na minha máquina
![image](https://github.com/BiancaMalta/Docker/assets/92928037/e4d05d69-3b50-4776-a49b-a12394084f90)

#### Os arquivos que gerei nessa atividade se encontram no [projeto-nginx](https://github.com/BiancaMalta/Docker/tree/main/projeto-nginx)
