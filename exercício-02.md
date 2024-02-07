# Exercício 02
## Elabora a resposta para as seguintes perguntas:
### O que é contêiner Docker?

#### É importante dividir essa pergunta em duas, primeiro cabe falar o que é contêiner para poder compreender o Docker. Muito similar as máquinas virtuais, o contêiner permite o isolamento completo de uma aplicação, diferindo por abstrair os detalhes do sistema operacional, isolando os processos de cada ferramente. Já o Docker é um software de código aberto usado para implantar aplicativos dentro de containers virtuais. Logo, um contêinder Docker facilita o compartilhamento de uma aplicação ou conjunto de serviços, incluindo todas as dependências deles em vários ambientes.

### Qual é a diferença entre uma imagem e um contêiner?
#### O container é o ambiente isolado, a estrutura executada, a instância runtime; pode ser parado, reiniciado ou removido, com preferencia a efêmeridade. Por outro lado, a imagem é mais perdurável, é reutlizada com frêquencia, ela possui as definições do que será executado, quais as bibliotecas e configurações estarão presentes no seu contêiner.

### O que é Docker Hub?

#### O Docker Hub é um repositório público e privado de imagens de containers, onde diversas empresas e pessoas podem publicar imagens pré-compiladas de soluções.
#### Para maiores informações clique [aqui](https://www.docker.com/products/docker-hub/)

### Por que é importante mapear portas ao executar contêineres?

#### O mapeamento de portas é necessário para que servidores web, bancos de dados ou qualquer aplicação se conecte com sistemas externos. Graças a isso, o aplicativo do seu container é exposto para o exterior, permitindo o acesso da sua máquina host. 

### O que é um Dockerfile e qual é sua função?

#### O Dockerfile é o meio, o passo a passo, que utilizamos para criar nossas próprias imagens. Resumidamente, é um ambiente onde se cria especificações para personalizar a execução do container.
![imagem2](https://github.com/BiancaMalta/Docker/blob/main/imagem2.png)





