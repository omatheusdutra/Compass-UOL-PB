SELECT Autor.codautor,
       Autor.nome,
       COUNT(Livro.cod) AS quantidade_publicacoes
FROM Autor
JOIN Livro ON Autor.codautor = Livro.autor
GROUP BY Autor.codautor,
         Autor.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1;