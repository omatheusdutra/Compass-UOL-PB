SELECT TBDEPENDENTE.cddep,
       TBDEPENDENTE.nmdep,
       TBDEPENDENTE.dtnasc,
       SUM(TBVENDAS.vrunt * TBVENDAS.qtd) AS valor_total_vendas
FROM TBDEPENDENTE
JOIN TBVENDEDOR ON TBDEPENDENTE.cdvdd = TBVENDEDOR.cdvdd
JOIN TBVENDAS ON TBVENDEDOR.cdvdd = TBVENDAS.cdvdd
WHERE TBVENDAS.status = 'Concluído'
GROUP BY TBDEPENDENTE.cddep,
         TBDEPENDENTE.nmdep,
         TBDEPENDENTE.dtnasc
HAVING valor_total_vendas > 0
ORDER BY valor_total_vendas ASC
LIMIT 1;