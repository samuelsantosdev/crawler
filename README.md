# Desafio Crawler - Feed Auto Esporte

## Dependências
* Docker version 18.09.7
* docker-compose version 1.24.1

## Ambiente
para iniciar o ambiente basta executar de dentro do diretório crawler:
```
$ docker-compose up -d
```
e acessar 127.0.0.1:5000

## Arquitetura
```
* app #diretório com o fonte da api django
`--->api
 `------->helpers
 `------->migrations #Estrutura inicial do banco
 `------->models 
 `------->serializers #Arquivos responsáveis para receber um ou mais objetos e criar uma nova estrutura para exibição
 `------->services #serviços, camada de abstração para regras de negócios etc, nesse caso parser do xml auto esporte
 `------->views #view User e Feed, responsáveis por tratar as requisições e expor os objetos serializados
 `------->tests.py #arquivo com todos os testes unitários
`--->crawler
 `------->settings.py #Configurações do Django e da aplicação, carregadas pelas variáveis de ambiente
 `------->url.py #Rotas da aplicação
`--->fixtures
 `------->users.json #Usuário inicial para testes, admin:qwe123
`--->logs #Logs da aplicação, requets e erros
* docker #diretório que contém o arquivos entrypoint da imagem Docker da api, migrations, fixtures e tests (app/logs/app.log)
* logs #logs do webserver, rodando na porta 5000
* nginx #arquivo de configuração do webserver nginx
* .env #variáveis de ambiente para o banco de dados postgres e aplicação django
* dev.env #variáveis de ambiente para auxiliar no desenvolvimento
* docker-compose.yml #arquivo do docker-compose
* Dockerfile #image da aplicação python django
```
