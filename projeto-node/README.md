# Projeto Node
### Nessa atividade subi uma aplicação simples para explorar mais a fundo o Dockerfile.
#### Alguns comando foram realizados:
##### Instalei os pacotes nodes 
```
# comando para criar um package.json para seu aplicativo.
npm init -y
# Express.js é um framework para Node.js que fornece recursos mínimos para construção de servidores web
npm install express
```
##### Criei uma imagem 
```
docker build -t projeto-node .
```
##### Construí um contêiner nomeado e mapeei sua porta 
```
docker run -d -p 3000:3000 --name node-aplicacao projeto-node
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/cca371db-fdb3-4f6b-992b-e1da192fb20d)
