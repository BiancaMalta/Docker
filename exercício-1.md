# Exercício 1
## Rode três contêineres com apache -> apache01 na porta 3000, apache02 na porta 4000 e apache03 na porta 5000
###### Para isso, executei os seguintes comandos:
```
docker run -d --rm -p 3000:80 httpd
docker run -d --rm -p 4000:80 httpd
docker run -d --rm -p 5000:80 httpd
```

