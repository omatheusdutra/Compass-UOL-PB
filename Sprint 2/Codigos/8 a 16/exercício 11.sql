SELECT v.cdcli AS cdcli,
       v.nmcli AS nmcli,
       SUM(v.qtd * v.vrunt) AS gasto
FROM tbvendas AS v
WHERE v.status = 'Concluído'
GROUP BY v.cdcli,
         v.nmcli
ORDER BY gasto DESC
LIMIT 1;