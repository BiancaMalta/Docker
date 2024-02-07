# Docker
[Documentação do Docker]()
<details>
  <summary> Comandos básicos </summary>

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
##### Construir uma imagem
```
mkdir exemplofile
cd exemplofile
vim exfile
docker image build -t exemplo:1.0 .
```
</details>
<details>
  <summary>Volumes</summary>

##### Tip bind
###### Eu já tenho o diretório e quero ele seja montado dentro do container
```
mkdir /opt/exemplo2
docker container run -ti --mount type-bind,src=/opt/exemplo2,dst=/exemplo2 ubuntu
```
###### Mesmo deletando, o conteudo do container nao se perde <br/>
###### Colocando ro antes da imagem, o container se torna apenas de leitura -> read only
[]()
##### Tipo volume
###### Criar volume
```
docker volume create exemplo3
```
###### Antigamente </br>
```
docker container create -v /data --name nomeexemplo ubuntu
docker run -d -p 5432:5434 --nome pgsql1 --volume-from nomeexemplo -e POSTGRESQL_USER=docker -e POSTGRESQL_PASS=docker -e POSTGRESQL_DB=docker kamui/postgresql
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
