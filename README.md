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

Nesse ambiente serão criados 3 serviços na sequência:

###DB:
Nesse serviço o banco postgres é inicializado com as credenciais do arquivos .env,
em uma rede privada

###API:
Uma imagem customizada do docker é gerada e 
após a criação dessa imagem são executados alguns comandos como:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/users.json
python manage.py test
```
O output desses comandos estarão disponíveis em app/api/logs/

###Front:
Expõe a aplicação (minha intenção era incluir também o gunicorn aqui)

Por padrão o Django cria o usuário "admin" senha "qwe123",
para poder ler o feed é necessário gerar um token JWT em
POST: 127.0.0.1:5000/api/token/
no body
```
{
    "username" : "admin",
    "password" : "qwe123"
}
```

Após isso solicitar os feeds em
GET: 127.0.0.1:5000/feed/
no header
```
Content-Type: application/json
Authorization: Bearer TOKEN_GERADO
```

Para criar novos usuários
POST 127.0.0.1:5000/users/
```
{
	"username" : "jose6",
	"password" : "qwe123qwe123",
	"email" : "testes@gmail.com",
	"is_staff" : true,
	"is_active" : true,
	"is_superuser" : true
}
```

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
