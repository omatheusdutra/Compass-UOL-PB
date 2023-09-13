SELECT DISTINCT Autor.nome
FROM Autor
JOIN Livro ON Livro.autor = Autor.codautor
JOIN Editora ON Livro.editora = Editora.codeditora
JOIN Endereco ON Editora.endereco = Endereco.codendereco
WHERE Endereco.estado NOT IN ('PARANÁ',
                              'SANTA CATARINA',
                              'RIO GRANDE DO SUL')
ORDER BY Autor.nome ASC;