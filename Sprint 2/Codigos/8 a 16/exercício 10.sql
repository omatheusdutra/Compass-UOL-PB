SELECT TBVENDEDOR.nmvdd AS vendedor,
       SUM(TBVENDAS.qtd * TBVENDAS.vrunt) AS valor_total_vendas,
       ROUND(SUM(TBVENDAS.qtd * TBVENDAS.vrunt) * TBVENDEDOR.perccomissao / 100, 2) AS comissao
FROM TBVENDEDOR
JOIN TBVENDAS ON TBVENDEDOR.cdvdd = TBVENDAS.cdvdd
WHERE TBVENDAS.status = 'Concluído'
GROUP BY TBVENDEDOR.nmvdd
ORDER BY comissao DESC;