# Created By: Andre Ramos da Silva

#### created using virtualenv \*

##### iniciando: virtualenv .

##### ativando o venv: source bin/activate

##### desativando venv: deactivate

### Docker compose com versão 5.7 do MySQL e o Adminer

#### iniciando, criando img e etc: docker-compose up -d

#### confifmando a rede do mysql: docker network ls

#### confirmando que esta ativo (porta 3306) e do Adminer (porta 8080): docker-compose ps

builda imagem
docker build .

builda imagem com o nome
docker build -t python_flask_backend .
-p 3000:3000
docker run python_flask_backend:latest

deleta imagem
docker rmi 474b696602

APAGAAR TUDO:
docker rmi -f \$(docker images -a -q)

roda aplicacao com o bash dentro do container
docker run -it -p 5000:5000 python_flask_backend:latest /bin/bash

roda aplicacao
docker run -p 5000:5000 python_flask_backend:latest

Apaga forcando
docker rm -f f2688fe23f08

docker-compose down

docker-compose up

docker run -it mysql bash

## preparando o mysql server

#### Via Adminer

Go to http://localhost:8080 or http://127.0.0.1:8080 and fill the credential. User: root  
password: rootpassword

no lado esquerdo va em importar, selecione o arquivo "scripts_sql.sql" e clique em executar.
