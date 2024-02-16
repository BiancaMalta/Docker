# Exercício 03
- Suba um contêiner com a imagem do nginx
- Crie um volume do tipo bind
- Mapeie a pasta que está a salvo seu arquivo index.html
- Após subir o contêiner, edite o arquivo e veja a mudança ocorrendo

## Para isso, executei os seguintes comandos:
### Entrei dentro da pasta da imagem do nginx e criei uma nova pasta para o volume bind 
```
cd projeto-nginx
mkdir volume-exercicio
```
### Executei o build da imagem
```
docker build -t nginximage .
```
### Subi o container com a imagem e o volume requisitado
```
docker run -d -p 80:80 --name exercicio03 -v volume-exercicio/:/usr/share/nginx/html/volume-exercicio nginximage
```
# Mapiei a pasta
```
docker inspect exercicio3
```
# Editer o arquivo
```
cd /usr/share/nginx/html/
echo "edição do arquivo">index.html
```
