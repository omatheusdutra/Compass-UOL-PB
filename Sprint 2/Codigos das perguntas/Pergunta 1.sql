SELECT Livro.cod AS CodLivro,
       Livro.titulo AS Titulo,
       Livro.autor AS CodAutor,
       Autor.nome AS NomeAutor,
       Livro.valor AS Valor,
       Livro.editora AS CodEditora,
       Editora.nome AS NomeEditora
FROM Livro
JOIN Autor ON Livro.autor = Autor.codautor
JOIN Editora ON Livro.editora = Editora.codeditora
ORDER BY Livro.valor DESC
LIMIT 10;