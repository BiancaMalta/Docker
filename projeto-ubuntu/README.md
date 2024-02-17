# Projeto Ubuntu
### A atividade foi desenvolvida com o propósito de compreender o que é um Dockerfile e como se cria um contêiner.
#### Para executar, fiz os seguintes passos:
##### Criei uma imagem 
###### Possuimos os mais diversos comandos com essa função
| Comando | Descrição |
| --- | --- |
| docker build |  Constrói uma imagem a partir de um Dockerfile (arquivo Docker) no diretório atual  |
| docker build https://github.com/.../ | Constrói uma imagem a partir de um repositório GIT remoto  |
| docker build -t imagename/tag | Constrói e identifica uma imagem, identificando-a com uma tag, para facilitar o monitoramento |
| docker build https://yourserver/file.tar.gz | Constrói uma imagem a partir de um arquivo tar remoto |
| docker build -t image:1.0-<<EOFFROM busyboxRUN echo “hello world”EOF | Constrói uma imagem a partir de um Dockerfile (arquivo Docker) que é enviado via STDIN |
###### Nesse projeto utilizei:
```
docker build -t projeto-ubuntu .
```
##### 
##### E subi o contêiner
```
docker run -d projeto-ubuntu
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/6ff73c75-ba4e-4c35-9f85-f88d380e261e)
###### A execução do container foi em background por ter passado a flag -d, já o nome e porta não foram setados, cabendo ao docker gerenciar isso.
