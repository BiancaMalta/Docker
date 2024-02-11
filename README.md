# Docker
### Durante o terceiro módulo do programa de capacitação DevOps da B3 em parceria com a Ada Tech, desenvolvemos algumas atividades de Docker. Nesse diretório, organizei em pastas os arquivos de cada atividade e abaixo deixei uma breve explicação sobre o tema. 
[Capacitação DevOps](https://ada.tech/sou-aluno/programas/b3-deva) </br>
[Documentação do Docker](https://docs.docker.com/)
<details>
  <summary> Comandos básicos </summary>
<img align="left" src="https://4linux.com.br/wp-content/uploads/2021/08/imagem-1024x594.png" alt='Direitos reservados a página 4linux' width="350" height="200" />

#### Enquanto as máquinas virtuais solucionaram o empecilho do uso de vários servidores físicos, o docker veio para solucionar o custo e o tempo gasto com a instalação, manutenção e configuração dos sistemas operacionais. A partir disso, surgiram os `containers`, responsáveis por emular uma aplicação com praticidade e portabilidade, bastando apenas um comando para que o ambiente inteiro em que um projeto foi construido, com suas versões e aplicações instaladas esteja rodando em outro lugar, caindo por terra a famosa frase "Mas na minha máquina funciona".

##### Listar os containers em execução
```
#sintase antiga
docker ps 
#sintase nova
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

[imagem demonstrando]()
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
> Após a criarção do container, se for necessário alterar as configurações, use:
> ```
> docker container update --cpus 0.2 'id do container'
> ```
##### Conectar ao container em segundo plano
```
docker container exec -ti 'id do container''comando que quero executar'
```
[imagem demonstrando]()
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

##### Construir uma imagem

<img align="left" src="https://i.stack.imgur.com/F837U.png"  width="180" height="130" />

##### Na construção de uma imagem, cada linha de instrução do Dockerfile, é responsável por criar uma camada, sendo todas read-only (não podem ser sobrescrita, a imagem é imutável), execeto a mais superficial, que será read-write (a que torna o container real). Contudo, a camada que o usuário possui permissão para interagir é excluída quando o container é removido, configuração esta, que os tornam muito eficientes em termos de recursos, pois vários contêineres podem ser executados usando a mesma imagem.  
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
- ENV -> variavel de ambiente
- COPY -> arquivo copiado e caminho 
- WORKDIR -> define diretório
- LABEL -> descrição da imagem
- VOLUME -> caminho para criar um volume  
- EXPOSE -> configura a porta
- ENTRYPOINT -> principal processo
- CMD -> parametros para o entrypoint

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

###### Como já mencionado, a camada read-write não foi projetada para armazenar dados persistentes. Caso haja a necessidade, é recomendado a utilização de `Volumes`, sua aplicação gera logs e arquivos de saída, permitindo a conservação dos dados, o compartilhamento do código fonte e o compartilhamento de dados entre os containers. Dependendo do caminho onde ele estará localizado, será um volume gerenciados pelo Docker ou volumes tipo bind.
##### Tipo bind
###### Esse volume apontam para um local especificado pelo usuário, sendo ótimo na hipotese de apontar vários containers para um armazenamento, entretanto tem riscos de sobreescrever dados.
```
mkdir /opt/exemplo2
docker container run -ti --mount type=bind,src=/opt/exemplo2,dst=/exemplo2 ubuntu
```
###### Mesmo deletando, o conteudo do container nao se perde <br/>
###### Colocando ro antes da imagem, o container se torna apenas de leitura -> read only
[]()
##### Gerenciado pelo Docker
###### Criados automaticameno pelo daemon Docker, esse tipo de volume vincula-se apenas a um único container
###### Criar volume
```
# Gerenciado pelo Docker
docker volume create <nome do volume>

docker run -d -p porta-local:porta-container --nome <nome do container> -v <nome do vomule>:<caminho para pasta> <nome da imagem>
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
#### Criar um backup
```
type=volume,src=dbdados,dst=/data --mount type+bind,src=/opt/backup,dst=/backup debian tar - cvf /bakup/bkp-banco.tar /data
```
</details> 
<details>
  <summary>Dockerhub</summary>
  
#### Subindo uma imagem

##### Para isso será necessário criar uma chave pública
```
gpg --generate-key
```
Esse comando irá pedir um nome, um email, uma senha e retornar a chave
```
pass init <chave pública>
```
Agora podemos fazer o login e publicar a imagem
```
docker log
docker image tag <id da imagem> <usuário do Dockerhub/nome da imagem:versão>
docker push <usuário do Dockerhub/imagem:versão>
```
#### Compartilhar um volume

</details>
<details>
  <summary>Docker Machine</summary>

##### Ferramenta para operar maquinas virtuais rodando Docker
##### Para começar, pasta passar suas credenciais 
```
aws_acess_key_id = <seu id>
aws_secret_access_key = <sua senha>
```
##### Para criar uma nova máquina
```
docker-machine create --drive amazone2 aws01
```
##### Tem várias opções, para conferir entre na [documentação](https://github.com/Nordstrom/docker-machine/blob/master/docs/drivers/aws.md)
</details>

## Autora
[![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bianca-malta/)
