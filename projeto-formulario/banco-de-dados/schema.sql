CREATE DATABASE IF NOT EXISTS banco_de_dados;  /**cria o banco de dados **/ 
USE banco_de_dados;    /**usa o banco de dados **/

CREATE TABLE IF NOT EXISTS `cliente`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(50),
    `cpf` CHAR(14),
    `email` VARCHAR(50),
    `hash_senha` VARCHAR(225),
    `data_nascimento` DATE,
    `estado_civil` VARCHAR(30)
);
