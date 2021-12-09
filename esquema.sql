CREATE DATABASE tienda;
use tienda;

create table clientes(
nombresCompleto varchar(100),
numeroCelular int unique key not null,
saldo float
);