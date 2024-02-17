# Projeto Php8
### Esse projeto como finalidade aprender a utilizar a volume bind.
##### Criei uma pasta para receber os dados
```
mkdir messages
```
##### E uma imagem 
```
docker build -t phpmessages .
```
##### Construi um container
```
docker run -d -p 80:80 --name php-aplicacao -v C:/home/bia/Projeto-Docker/projeto-php8/messages:/var/www/html/messages phpaplicacao
```
##### Como consequência, todas as mensagens escritas no `localhost/index.php`, vão ser salvar na pasta messages
![image](https://github.com/BiancaMalta/Docker/assets/92928037/4b41e7b8-e910-4feb-a5db-524b4761b66a)
##### É possível ler as mensagens pelo `localhost/messages/msg-0.txt` ou entrando no terminal do container
> [!CAUTION]
> O volume bind é gerenciado pelo usuário, se for deletado algo da pasta que está na máquina, também será deletado do container.
