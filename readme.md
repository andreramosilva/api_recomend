# Created By: Andre Ramos da Silva

### Docker compose com versão 5.7 do MySQL e o Adminer

#### iniciando, criando img e etc: docker-compose up -d

#### confifmando a rede do mysql: docker network ls

#### confirmando que esta ativo (porta 3306) e do Adminer (porta 8080): docker-compose ps

## preparando o mysql server

#### Via Adminer

Go to http://localhost:8080 or http://127.0.0.1:8080 and fill the credential. User: root  
password: rootpassword

no lado esquerdo va em importar, selecione o arquivo "scripts_sql.sql" e clique em executar.

### swagger

http://127.0.0.1:5000/swagger/

### testing library

https://nose.readthedocs.io/en/latest/usage.html

### rodar localmente ** (mysql e o adminier precisam estar ligados no docker para funcionar) **

pip install -r requirements.txt
python app.py
