SELECT Autor.codautor,
       Autor.nome,
       Autor.nascimento,
       COUNT(Livro.cod) AS quantidade
FROM Autor
LEFT JOIN Livro ON Autor.codautor = Livro.autor
GROUP BY Autor.codautor,
         Autor.nome,
         Autor.nascimento
ORDER BY Autor.nome ASC;