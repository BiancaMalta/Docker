# Exercício 04
## Quais são as boas práticas de mercado para configurar e gerir Redes no Docker?

#### Vimos em aula o que são `Redes Docker`, após esse passo, torna-se de suma importância aprender a como configura-las e gerenciá-las. Para maior praticidade, o Docker oferece o comando docker network seguido dos parâmetros:
- `create <nome/ID da rede>` -> cria uma nova rede
- `ls` -> lista as redes disponíveis exibindo seu nome, ID e drive de rede
- `inspect <nome/ID da rede>` -> especifica detalhes sobre uma rede
- `rm <nome/ID da rede>` -> remove uma rede do Docker
- `prune` –> remove todas as redes não utilizadas
- `connect` –> conecta uma rede a um contêiner
- `disconnect` –> desconecta um contêiner de uma rede
#### A fim de garantir a segurança e o bom funcionamento de suas redes, deve-se adotar a praticar de criar nomes descritivos, limitar e monitorar o tráfego dos seus contêineres e utilizar o `driver de rede` correto para o seu caso de uso. Sobre os drivers, cabe relembrar algumas diferenças:
- `Bridge` (rede padrão): os contêineres se comunicam uns com os outros e também com o host. São de grande utilidade quando a aplicação é executada em uma única máquina.
- `Host`: contêineres autônomos, remove o isolamento de rede entre o container e o host. Isso pode ser útil para casos de uso específicos onde o desempenho da rede é crítico. 
- `None`: contêiner não tem acesso à rede externa. Essa opção é útil quando precisa isolar completamente um contêiner da rede.
#### Em resumo, essa camada de abstração fornecida pelo Docker - as Redes - permite gerenciar a comunicação entre os contêineres, boas práticas facilitam a administração de como suas aplicações se comunicam entre si.
