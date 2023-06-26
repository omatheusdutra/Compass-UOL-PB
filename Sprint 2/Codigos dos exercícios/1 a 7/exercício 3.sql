SELECT COUNT(*) AS quantidade,
       E.nome,
       EN.estado,
       EN.cidade
FROM Livro L
INNER JOIN Editora E ON L.editora = E.codeditora
INNER JOIN Endereco EN ON E.endereco = EN.codendereco
GROUP BY E.codeditora
ORDER BY quantidade DESC
LIMIT 5;