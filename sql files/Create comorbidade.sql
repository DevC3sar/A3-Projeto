create database Projeto;

create table comorbidade (
	id int AUTO_INCREMENT primary key,
	paciente_id int,
    situacao VARCHAR(255),
    comorbidade VARCHAR(255),
    foreign key(paciente_id) references paciente(id)
);    
    