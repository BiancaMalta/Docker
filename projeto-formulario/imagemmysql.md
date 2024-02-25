# Imagem MySQL- Descrição
Esta imagem configura um banco de dados MySQL pronto para se conectar a uma aplicação web desenvolvida em PHP. A aplicação possui um processo simplificado de levantamento de dados cadastrais, fluxo de dados este tratado pelo MySQL. O usuário tem a permissão de inserir o nome, o CPF, um e-mail, uma senha, a data de nascimento e o estado civil, resultando em um registro tabelado. Por intermédio do Docker, virtualizei todas as etapas e com o Docker Compose gerenciei o processo.

## Componentes e Referências
- [Imagem da aplicação PHP](https://hub.docker.com/repository/docker/biancamalta/php-projetoformulario)
- [Aplicação PHP](https://github.com/BiancaMalta/Docker/blob/main/projeto-formulario/aplicacao/process.php)
- [Front-end](https://github.com/BiancaMalta/Docker/blob/main/projeto-formulario/aplicacao/index.html)
- [Banco de dados](https://github.com/BiancaMalta/Docker/blob/main/projeto-formulario/banco-de-dados/schema.sql)
- [DockerCompose]( https://github.com/BiancaMalta/Docker/blob/main/projeto-formulario/docker-compose.yml)
- [Fonte do projeto](https://github.com/BiancaMalta)

## Como usar
### Construção da imagem 

#### Com Alterações
Caso deseje realizar alguma alteração ou utilizar essa imagem como base para outros projetos, será necessário compreender um pouco a estrutura de um `Dockerfile`.
##### Anatomia
```
FROM -> imagem base
RUN -> comandos de construção
ENV -> variável de ambiente
COPY -> arquivo copiado e caminho
WORKDIR -> define diretório
LABEL -> descrição da imagem
VOLUME -> caminho para criar um volume
EXPOSE -> configura a porta
ENTRYPOINT -> principal processo
CMD -> parâmetros para o entrypoint
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
 Dessa forma, não é preciso realizar o `build`.

#### Execução da imagem 
Nessa etapa, iremos executar o container e passar algumas variáveis de ambiente. Usar a configuração fornecida não é o ideal no quesito segurança, recomendo personalizá-la. As variáveis são:
- `MYSQL_ROOT_PASSWORD`: Senha para acessar o banco dentro do container;
- `MYSQL_DATABASE`: Banco de dados a ser criado;
- `MYSQL_USER`: Usuário para ter acesso ao banco de dados;
- `MYSQL_PASSWORD`: Senha do usuário para ter acesso ao banco de dados;

 A respeito do projeto desenvolvido, eu executei primeiro a imagem do MySQL e depois a do PHP :
```
docker run -d -p 3306:3306 -d --name container-bd -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=banco_de_dados -e MYSQL_USER=MainUser -e MYSQL_PASSWORD=MainPassword biancamalta/mysql-projetoformulario:1.0.0

docker run -d -p 5000:5000 --name container-php  biancamalta/php-projetoformulario:1.0.0

```
## Conecção 
 Com as imagens em execução, criei e conectei-as a um drive de rede `brigde`:
```
docker network create rede
docker network conect container-bd
docker network conect container-php
```
 Agora, os dados inseridos em http://localhost:80 vão ser armazenados e organizados pelo MySQL.

## Acesso e Operações
 Ao acesse a aplicação web pelo navegador, você irá se deparar com a seguinte interface:
</br><img  src="https://github.com/BiancaMalta/Docker/assets/92928037/4c4e9281-9896-49e6-afa9-68d400c6e65b" width="50%"></br>
E os dados cadastrados vão estar estruturados da seguinte maneira:
</br> <img  src="https://github.com/BiancaMalta/Docker/assets/92928037/c0a5e2a5-07b3-4572-a3ee-f37efa00b732" width="80%">
## Autora
[![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bianca-malta/)
