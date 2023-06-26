SELECT Editora.codeditora AS CodEditora,
       Editora.nome AS NomeEditora,
       COUNT(Livro.cod) AS QuantidadeLivros
FROM Editora
JOIN Livro ON Editora.codeditora = Livro.editora
GROUP BY Editora.codeditora,
         Editora.nome
ORDER BY COUNT(Livro.cod) DESC
LIMIT 5;