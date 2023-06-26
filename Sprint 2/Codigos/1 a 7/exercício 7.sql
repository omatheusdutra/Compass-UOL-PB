SELECT Autor.nome
FROM Autor
LEFT JOIN Livro ON Autor.codautor = Livro.autor
WHERE Livro.cod IS NULL
ORDER BY Autor.nome ASC;