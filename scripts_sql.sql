CREATE DATABASE dbuser_amigo_recomend;

 use dbuser_amigo_recomend;

CREATE TABLE user_amigo (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(30) NOT NULL,
nome_amigo VARCHAR(30) NOT NULL,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);



INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('ana','carlos');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('ana','joao');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('ana','maria');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('ana','vinicius');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('carlos','ana');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('joao','ana');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('maria','ana');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('maria','vinicius');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('vinicius','ana');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('vinicius','maria');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('joao','luiza');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('luiza','joao');

-- query de recomendacao 
-- select * from 
-- (select nome from user_amigo
-- where nome_amigo <> 'ana'
-- and nome <> 'ana') nao_amigo
-- left join 
-- (select nome_amigo from user_amigo 
-- where nome = 'ana') amigo
-- on nome = nome_amigo
-- where nome_amigo is null



