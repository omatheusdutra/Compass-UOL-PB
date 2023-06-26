SELECT TBVENDAS.cdpro,
       TBVENDAS.nmcanalvendas,
       TBVENDAS.nmpro,
       SUM(qtd) AS quantidade_vendas
FROM TBVENDAS
WHERE status = 'Concluído'
GROUP BY TBVENDAS.cdpro,
         TBVENDAS.nmcanalvendas,
         TBVENDAS.nmpro
ORDER BY quantidade_vendas
LIMIT 10;