# Descrição
Esta imagem configura um banco de dados MySQL pronto para se conectar a uma aplicação web simples desenvolvida em PHP.A aplicação possui um processo simplificado de levantamento de dados cadastrais,fluxo de dados este, que é tratado pelo MySQL. Os usuários tem a permissão de visualizar, adicionar ou modificar registros na tabela por intermédio de uma interface web simples.


## Componentes e Referências
- Aplicação PHP: 
- Banco de Dados MySQL: 
- DockerCompose:
- Repositório com o projeto completo:
- Fonte do projeto:github

## Como utilizar
### Construção da imagem 
#### Com Alterações
Caso deseje realizar alguma alteração ou utilizar essa imagem como base para outros projetos, será necessário compreender um pouco a estrutura de um `Dockerfile`.
##### Anatomia
```
FROM -> imagem base
RUN -> comandos de construção
ENV -> variavel de ambiente
COPY -> arquivo copiado e caminho
WORKDIR -> define diretório
LABEL -> descrição da imagem
VOLUME -> caminho para criar um volume
EXPOSE -> configura a porta
ENTRYPOINT -> principal processo
CMD -> parametros para o entrypoint
```
 Em seguida, execute os comandos para construir a imagem Docker:
```
docker build -t nova-imagem .
```
#### Sem alterações
 Para baixar a imagem disponibilizada sem realizar modificações:
```
docker pull biancamalta/mysql-projetoformulario:1.0.0
```
 Dessa forma, não precisamos realizar o `build`.
### Execução da imagem 
 A respeito do projeto desenvolvido, antes de executar a imagem da aplicação, eu já havia executado a do banco de dados. Portanto, a ordem dos comandos foram:
```
docker run -d --name container-bd -e MYSQL_ROOT_PASSWORD:container-bd -e MYSQL_USER=bianca -e MYSQL_PASSWORD=senha biancamalta/mysql-projetoformulario:1.0.0

docker run --name container-php -p 5000:5000 -e APLICACAO_DB_HOST:container-bd:3306 -e APLICACAO_DB_NAME:container-php -e APLICACAO_USER=bianca -e APLICACAO_PASSWORD=senha  biancamalta/php-projetoformulario:1.0.0

```
### Conecção 
 Com as imagens em execução, criei e conectei a um drive de rede brigde
```
docker network create rede
docker network conect container-bd
docker network conect container-php
```
 Agora, os dados inseridos em http://localhost:5000 vão ser armazenados e organizados pelo MySQL.

## Acesso e Operações
 Ao acesse a aplicação web pelo navegador, você irá se deparar com a seguinte interface:
 []()
 Os dados cadastrados são armazenado e tratados pelo MySQL, viabilizando uma maior organização e praticidade.
 []()


## Autora
[![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bianca-malta/)


