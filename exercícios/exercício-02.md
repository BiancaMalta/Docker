# Exercício 02
## Elabora a resposta para as seguintes perguntas:
### O que é contêiner Docker?

#### É importante dividir essa pergunta em duas, primeiro cabe falar o que é contêiner para poder compreender o Docker. Muito similar às máquinas virtuais, o contêiner permite o isolamento completo de uma aplicação, diferindo por abstrair os detalhes do sistema operacional, isolando os processos de cada ferramenta. Já o Docker é um software de código aberto usado para implantar aplicativos dentro de contêineres virtuais. Logo, um contêiner Docker facilita o compartilhamento de uma aplicação ou conjunto de serviços, incluindo todas as dependências deles em vários ambientes.

### Qual é a diferença entre uma imagem e um contêiner?
#### O contêiner é o ambiente isolado, a estrutura executada, a instância runtime; pode ser parado, reiniciado ou removido, com preferência à efemeridade. Por outro lado, a imagem é mais perdurável, é reutilizada com frequência, ela possui as definições do que será executado, quais as bibliotecas e configurações estarão presentes no seu contêiner.
### O que é Docker Hub?

#### O Docker Hub é um repositório público e privado de imagens de contêineres, onde diversas empresas e pessoas podem publicar imagens pré-compiladas de soluções.
#### Para mais informações, clique [aqui](https://www.docker.com/products/docker-hub/)

### Por que é importante mapear portas ao executar contêineres?

#### O mapeamento de portas é necessário para que servidores web, bancos de dados ou qualquer aplicação se conecte com sistemas externos. Graças a isso, o aplicativo do seu contêiner é exposto para o exterior, permitindo o acesso da sua máquina host.

### O que é um Dockerfile e qual é sua função?

#### O Dockerfile é o meio, o passo a passo, que utilizamos para criar nossas próprias imagens. Resumidamente, é um ambiente onde se criam especificações para personalizar a execução do contêiner.
![imagem2](https://github.com/BiancaMalta/Docker/blob/main/imagem2.png)





