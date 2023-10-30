SELECT * 
FROM paciente;

SELECT *
FROM comorbidade;

SELECT *
FROM paciente
LEFT JOIN comorbidade
ON paciente.id = comorbidade.paciente_id;

SELECT *
FROM paciente
LEFT JOIN comorbidade
ON paciente.id = comorbidade.paciente_id
WHERE comorbidade.paciente_id IS NULL;

SELECT *
FROM paciente
RIGHT JOIN comorbidade
ON paciente.id = comorbidade.paciente_id;

SELECT *
FROM paciente
RIGHT JOIN comorbidade
ON paciente.id = comorbidade.paciente_id
WHERE paciente.id IS NULL;

-- simulação full outer join. MySQL não suporta FULL OUTER JOIN
SELECT * FROM paciente 
LEFT JOIN comorbidade ON paciente.id = comorbidade.paciente_id
UNION 
SELECT * FROM paciente 
RIGHT JOIN comorbidade ON paciente.id = comorbidade.paciente_id;

-- simulação full outer join. MySQL não suporta FULL OUTER JOIN
SELECT * FROM paciente 
LEFT JOIN comorbidade ON paciente.id = comorbidade.paciente_id
WHERE paciente.id IS NULL OR
	  comorbidade.paciente_id IS NULL
UNION 
SELECT * FROM paciente 
RIGHT JOIN comorbidade ON paciente.id = comorbidade.paciente_id
WHERE paciente.id IS NULL OR
	  comorbidade.paciente_id IS NULL;
      
SELECT *
FROM paciente
INNER JOIN comorbidade
ON paciente.id = comorbidade.paciente_id;