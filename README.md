# Docker 🐋
<img align="right" src="https://i.picasion.com/pic92/464c9f3c112406d4aa886558a6da44c8.gif" width="27%" />

### Durante o terceiro módulo do programa de capacitação DevOps da B3 em parceria com a Ada Tech, desenvolvemos algumas atividades de Docker. Nesse diretório, organizei em pastas os arquivos de cada atividade e abaixo deixei uma breve explicação sobre o tema. 
[Capacitação DevOps](https://ada.tech/sou-aluno/programas/b3-deva) </br>
[Documentação do Docker](https://docs.docker.com/)

## Do Zero a Marinheiro 🚢📦📦
<details>
  <summary> Comandos básicos </summary>
<img align="left" src="https://4linux.com.br/wp-content/uploads/2021/08/imagem-1024x594.png" alt='Direitos reservados a página 4linux' width="350" height="200" />

#### Enquanto as máquinas virtuais solucionaram o empecilho do uso de vários servidores físicos, o `Docker` veio para solucionar o custo e o tempo gasto com a instalação, manutenção e configuração dos sistemas operacionais. A partir disso, surgiram os `containers`, responsáveis por emular uma aplicação com praticidade e portabilidade, bastando apenas um comando para que o ambiente inteiro em que um projeto foi construído, com suas versões e aplicações instaladas, esteja rodando em outro lugar, caindo por terra a famosa frase "Mas na minha máquina funciona".

##### Listar os containers em execução
```
#síntase antiga
docker ps 
#síntase nova
docker container ls 
```
##### Listar todos os containers
```
docker container ls -a
```
##### Executar um container
```
docker container run
```
###### Cabe mencionar algumas flags:
| Flag | Descrição |
| --- | --- |
| -ti |  cria um shell bash interativo |
| --rm | o container será removido após a execução |
| -d | roda um container como deamon |
| -m | limita a quantidade de memória |
| --cpus | seta o core |
| -p porta-local:porta-container | configura as portas |
| -P| porta aleatória para o local:porta especificada na imagem|
| --name <nome da imagem> | personaliza o nome |
> [!TIP]
> Para sair de um container basta usar Ctrl + pq, já para matar Ctrl + d* </br>

##### Parar um container
```
docker container stop 'nome/id do container'
```
##### Pausar os processos
```
docker container pause 'id do container'
```
##### Retomar os processos
```
docker container unpause 'id do container'
```
##### Reiniciar um container
```
#Caso já esteja parado
docker container start 'nome/id do container'
#Caso esteja em execução
docker container restart 'nome/id do container'
```
##### Conectar novamente ao container
```
docker container attach 'nome/id do container'
```
> [!IMPORTANT]
> Após a criação do container, se for necessário alterar as configurações, use:
> ```
> docker container update --cpus 0.2 'id do container'
> ```
##### Executar um comando no container
```
docker container exec -it 'id do container''comando que quero executar'
```
###### Dessa forma, é possível entrar no bash do container
<img src="https://github.com/BiancaMalta/Docker/assets/92928037/822d2426-89ce-4a33-a35e-31c60fc396bb" width="70%" />

##### Inspecionar
```
docker container inspect 'id do container'
```
##### Remover container parado
```
docker container prune
```
##### Ver o histórico e continuar executando
```
docker container logs -f 'id do container'
```
##### Consumo de recursos
```
docker container stats 'id do container'
```
##### Ver processos em execução
```
docker container top 'id do container'
```
</details>
<details>
  <summary>Imagem</summary>

<img align="left" src="https://i.stack.imgur.com/F837U.png"  width="180" height="130" />

#### Na construção de uma `imagem`, cada linha de instrução do `Dockerfile`, é responsável por criar uma camada, sendo todas read-only (não podem ser sobrescrita, a imagem é imutável), execeto a mais superficial, que será read-write (a que torna o container real). Contudo, a camada que o usuário possui permissão para interagir é excluída quando o container é removido, configuração esta, que os tornam muito eficientes em termos de recursos, pois vários contêineres podem ser executados usando a mesma imagem.  
##### Construir uma imagem
```
mkdir exemplofile
cd exemplofile
vim Dockerfile
docker image build -t <nome da imagem>:<versão> .
```
##### Dockerfile
###### Por definição, imagem é um arquivo que inclui código, bibliotecas, dependências e configurações. Quando executamos o 'vim' do comando anterior, precisamos deixar setado algumas especificações dentro da imagem.
<img align="right" src="https://github.com/BiancaMalta/Docker/blob/main/imagem2.png" width="340" height="260" />

- FROM -> imagem base
- RUN -> comandos de construção
- ENV -> variável de ambiente
- COPY -> arquivo copiado e caminho 
- WORKDIR -> define diretório
- LABEL -> descrição da imagem
- VOLUME -> caminho para criar um volume  
- EXPOSE -> configura a porta
- ENTRYPOINT -> principal processo
- CMD -> parâmetros para o entrypoint

##### Baixar imagens
```
docker pull <nome da imagem>
```
##### Ver todas as imagens
```
docker image ls
```
##### Remover imagem
```
docker rmi <id ou nome da imagem>
```

</details>
<details>
  <summary>Volumes</summary>

#### Como já mencionado, a camada read-write não foi projetada para armazenar dados persistentes. Caso haja a necessidade, é recomendado a utilização de `Volumes`, sua aplicação gera logs e arquivos de saída, permitindo a conservação dos dados, o compartilhamento do código fonte e o compartilhamento de dados entre os containers. Dependendo do caminho onde ele estará localizado, será um volume gerenciados pelo Docker ou volumes tipo bind.

##### Tipo bind
###### Esse volume apontam para um local especificado pelo usuário, sendo ótimo na hipótese de apontar vários containers para um armazenamento, entretanto tem riscos de sobreescrever dados e é administrado somente pelo usuário.
```
mkdir exemplo2
docker container run -it -v $(pwd)/exemplo2:<diretóriodentro do container> <nome da imagem>
```
###### Colocando ro antes da imagem, o container se torna apenas de leitura -> read only

##### Gerenciado pelo Docker
###### Criados automaticameno pelo daemon Docker, esse tipo de volume vincula-se apenas a um único container
```
# anônimo
docker run -it -v /<diretóriodentro do container> <nome da imagem>
# nomeado
docker volume create <nome volume>
docker run -d -p porta-local:porta-container --nome <nome do container> -v <nome volume>:<caminho para pasta dentro do container> <nome da imagem>
```
> [!IMPORTANT]
> Se você precisar passar informações sobre o drive de volume, o recomendado é:
> ```
> --mount 'type=<tipo do volume>,source=<diretório do nosso sistema>,destination=<diretório dentro do container>'
> ```

##### Uma forma de testa seu volume 
```
# entre dentro do terminal do container
docker exec -it <nome do terminal> /bin/bash
# entre dentro da pasta que foi destinado o volume
cd <caminho>/
# crie uma pasta qualquer
echo "Testando Volume" > teste.txt
# saia do container e vá ao diretorio do volume
# é esperado que todas as alterações do container estejam na máquina local
```
##### Ver todos os volumes
```
docker volume ls
```
##### Apagar volume
```
docker volume rm <nome/id do volume>
```
##### Inspecionar volume
```
docker volume inspect exemplo3
```
##### Adicionar volume a um container
```
docker container run -ti --mount type-volume,src=exemplo3,dst=/exemplo2 ubuntu
```
##### Apagar volumes que não estao sendo utilizados
```
docker volume prune
 ```
</details> 
<details>
  <summary>Dockerhub</summary>
<img align="right" src="https://github.com/BiancaMalta/Docker/assets/92928037/808f312c-44bb-4f9c-aae3-b3616a41e516"  width="45%" />

#### O `Docker Hub` é um repositório público e privado de imagens de containers, onde diversas empresas e pessoas podem publicar imagens pré-compiladas de soluções.Para maiores informações clique [aqui](https://www.docker.com/products/docker-hub/).
 
##### Subindo uma imagem

###### Para isso será necessário criar uma chave pública
```
gpg --generate-key
```
###### Esse comando irá pedir um nome, um email, uma senha e retornar a chave
```
pass init <chave pública>
```
###### Agora podemos fazer o login e publicar a imagem
```
docker login
docker image tag <id da imagem> <usuário do Dockerhub/nome da imagem:versão>
docker push <usuário do Dockerhub/imagem:versão>
```
###### Para baixar a imagem disponibilizada
```
docker pull <usuário do Dockerhub/imagem:versão>
```
</details>
<details>
  <summary>Docker Machine</summary>

<img align="left" src="https://github.com/BiancaMalta/Docker/assets/92928037/b3c4c302-fa39-4769-a68f-ee673f68cdcf"  width="30%" />

#### O `Docker Machine` é uma ferramente para operar máquinas virtuais com Docker, sendo compatível com diferentes provedores de infraestrutura (Amazon Web Services, Google Cloud Platform e Microsoft Azure). Por conseguinte, possibilita a escalabilidade, além disso, ele oferece suporte a diversos sistemas operacionais.
##### Para começar, basta passar suas credenciais 
```
aws_acess_key_id = <seu id>
aws_secret_access_key = <sua senha>
```
##### Criar uma nova máquina
```
docker-machine create --drive amazone2 aws01
```
##### Para outras opções, confira a [documentação](https://github.com/Nordstrom/docker-machine/blob/master/docs/drivers/aws.md).
</details>
<details>
  <summary>Redes</summary>

#### Existem tem pilares para o uso de `redes`:
- Comunicação entre containers/ host/ plataforma
- Isolamento de container
- Orquestração do ambiente
#### Destrinchando essas caracteristicas, temos algumos tipos de redes:
#####  Bridge (rede padrão) 
###### Comunicação entre containers no mesmo host.
##### None 
###### Isolado, nao possui acesso nem externo e nem de outros containers, não tem IP. Muito útil quando não há a necessidade de conectividade de rede dentro do container.
##### Host
###### Faz uma ponte/ IP do container = IP da máquina. Não sendo possível iniciar vários containers com a mesma porta. Logo, se eu executar os seguintes comandos:
```
docker container run -p 80:80 --name container_1 -d --network rede imagem_1:versão
docker container run -p 80:80 --name container_2 -d --network rede imagem_2:versão
```
###### Em poucos segundos eles entraram em conflito e um dos container irá cair
##### Para conferir qual tipo de rede você possui
```
docker network ls
```
##### Criar uma nova rede
```
docker network creat <nome da rede>
```
##### Conferir se possui conflitos
```
docker network inspect <nome da rede>
```
##### Remover rede
```
# Uma rede em especifico
docker network rm <nome da rede>
# Todas que não estão sendo utilizadas
docker network prune
```
##### Para desconectar/conectar um container em uma rede
```
# Desconectar
docker network disconect <nome do container>
# Conectar
docker network conect <nome do container>
```
##### Comunicação DNS
```
docker container run -d --name container_1 imagem_1:versão
docker container run -d --name container_2 --link container_1 imagem_2:versão
```
###### Para conferir, basta fazer o teste de ping dentro do container
```
docker container exec -it container_1 ping container_2
```
###### A desvantagem é que o oposto nao funciona
###### O recomendado é criar redes próprias
```
docker network create -d bridge rede
docker container run -d --name container_1 --network rede imagem_1:versão
docker container run -d --name container_2 --network rede imagem_2:versão
```
###### Agora, independente da ordem que for efetuada o teste de ping, o comando irá funcionar
</details>
<details>
  <summary>Docker Compose</summary>

#### Docker Compose é um aquivo escrito em YAML, muito semelhando ao Dockerfile, que torna possível manipular vários container ao mesmo tempo. Nele está descrito toda a infraestrutura, variáveis de ambiente e até mesmo definido o comportamento do Docker caso um dos container venha a falhar. Em síntese, ao invés do administrador executar o `docker run` na mão e subir os serviços separados, linkando os containers das aplicações manualmente, temos um único arquivo.
<img align="right" src="https://github.com/BiancaMalta/Docker/blob/main/dockercompose.png" width="200" height="200" />

#### Usar o Docker Compose é um processo de três etapas:
1. Defina o ambiente
2. Defina os serviços
3. Por último, execute docker compose up
##### Anatomia
```
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
  redis:
    image: redis
```
#### Comandos: 
##### Primeiros passos
```
docker-compose --version
```
###### Se for preciso instalar, acesse a [documentação](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
##### Executar o docker-compose
```
docker-compose up
```
###### Para executar em segundo plano, basta colocar a flag `-d`
###### Na hipótese de ter ocorrido alguma alguma alteração na imagem, use a flag `--build`

##### Matar os containers que subiu com o comando anterior
```
docker-compose down
```
###### Usando a flag `-v` os volumes são deletados
##### Parar todos os containers
```
docker-compose stop
```
##### Remover todos os containers
```
docker-compose rm -f
```
##### Ver o log de todos os containers
```
docker-compose logs -f
```
##### Construir os containers sem inicializá-los
```
docker-compose build
```
![image](https://github.com/BiancaMalta/Docker/assets/92928037/a23e4958-c81e-416f-86a5-43d603a1cb53)

</details>

## Autora 🐳
[![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bianca-malta/)
