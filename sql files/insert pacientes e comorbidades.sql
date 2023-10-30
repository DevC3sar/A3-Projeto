INSERT INTO paciente (nome, cpf , idade, endereco) 
VALUES 
	('Charlotte', '00000000000', '35', 'Rua 1'),
    ('Oliver', '11111111111', '63', 'Rua 2'),
    ('Helena', '22222222222', '89', 'Rua 3'),
    ('Miguel', '33333333333', '46', 'Rua 4'),
    ('Olivia', '44444444444', '91', 'Rua 5'),
    ('Noah', '55555555555', '4', 'Rua 6'),
    ('Emma', '66666666666', '88', 'Rua 7'),
    ('Liam', '77777777777', '41', 'Rua 8'),
    ('Kiara', '88888888888', '100', 'Rua 9'),
    ('Mohammad', '99999999999', '11', 'Rua 10'),
    ('Sophia', '10000000000', '15', 'Rua 11'),
    ('Theo', '20000000000', '56', 'Rua 12'),
    ('Martina', '30000000000', '34', 'Rua 13'),
    ('Francesco', '40000000000', '78', 'Rua 14'),
    ('Mia', '50000000000', '24', 'Rua 15'),
    ('Louis', '60000000000', '67', 'Rua 16'),
    ('Himari', '70000000000', '29', 'Rua 17'),
    ('Nagisa', '80000000000', '9', 'Rua 18')
;
    
INSERT INTO comorbidade (comorbidade.paciente_id, situacao, comorbidade)  
VALUES   
	(1, 'Grave', 'Diabetes'),
    (1, 'Moderado', 'Hipertensão Arterial'),
    (2, 'Leve', 'Doença renal'),
    (2, 'Gravíssimo', 'Imunocomprometidos'),
    (2, 'Moderado', 'Obesidade mórbida'),
    (3, 'Gravíssimo', 'Cirrose'),
    (3, 'Leve', 'Insuficiência Cardíaca'),
    (4, 'Grave', 'Hipertensão pulmonar'),
    (4, 'Gravíssimo', 'Arritmias cardíacas'),
    (5, 'Moderado', 'Acidente vascular cerebral'),
    (5, 'Gravíssimo', 'Ataque isquêmico'),
    (6, 'Leve', 'Demência Vascular'),
    (6, 'Leve', 'Paralisia Cerebral'),
    (7, 'Moderado', 'Esclerose Múltipla'),
    (7, 'Grave', 'Deficiência neurológica'),
    (8, 'Gravíssimo', 'Diabetes'),
    (8, 'Leve', 'Hipertensão Arterial'),
    (9, 'Moderado', 'Doença renal'),
    (9, 'Gravíssimo', 'Imunocomprometidos'),
    (10, 'Moderado', 'Cirrose'),
    (10, 'Leve', 'Insuficiência Cardíaca'),
    (11, 'Gravíssimo', 'Hipertensão pulmonar'),
    (11, 'Gravíssimo', 'Arritmias cardíacas'),
    (12, 'Grave', 'Acidente vascular cerebral'),
    (12, 'Gravíssimo', 'Ataque isquêmico'),
    (13, 'Grave', 'Demência Vascular'),
    (13, 'Gravíssimo', 'Paralisia Cerebral'),
    (14, 'Grave', 'Esclerose Múltipla'),
    (14, 'Grave', 'Deficiência neurológica'),
    (15, 'Leve', 'Diabetes'),
    (15, 'Gravíssimo', 'Hipertensão Arterial')
;

INSERT INTO comorbidade (situacao, comorbidade)  
VALUES
	('Gravíssimo', 'Doença renal'),
    ('Moderado', 'Imunocomprometidos'),
    ('Gravíssimo', 'Obesidade mórbida'),
    ('Grave', 'Cirrose'),
    ('Leve', 'Insuficiência Cardíaca')
;