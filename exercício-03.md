# Exercício 03
- Suba um contêiner com a imagem do nginx
- Crie um volume do tipo bind
- Mapeie a pasta que está a salvo seu arquivo index.html
- Após subir o contêiner, edite o arquivo e veja a mudança ocorrendo

## Para isso, executei os seguintes comandos:
### Entrei dentro da pasta da imagem do nginx e criei uma nova pasta para o volume bind 
(crio o volume aqui ou em outro lugar? como faço pra colocar o index ali dentro?)
```
cd projeto-nginx
mkdir volumeex
```
### Subi o container com a imagem e o volume requisitado
(preciso fazer o bild novamente?)
```
docker run -d -p 80:80 --name exercicio03 -v volumeex/:/usr/share/nginx/html projeto-nginx
```
# Mapiei a pasta
```
cd /usr/share/nginx/html/
ls
pwd
```
# Editer o arquivo
```
echo "edição do arquivo">index.html
```
