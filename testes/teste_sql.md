# Teste prático de SQL

Tabela `pedidos (id, cliente_id, valor, data)`

1. Total vendido por mês
2. Os 3 clientes que mais compraram
3. Para cada cliente, o valor do primeiro pedido
4. Clientes que compraram em janeiro e não compraram em fevereiro de 2026
5. Variação percentual do faturamento de um mês para o outro

## Gabarito

```sql
-- 1
SELECT DATE_TRUNC('month', data) AS mes, SUM(valor) AS total
FROM pedidos GROUP BY 1 ORDER BY 1;

-- 2
SELECT cliente_id, SUM(valor) AS total
FROM pedidos GROUP BY cliente_id ORDER BY total DESC LIMIT 3;

-- 3
WITH ordenado AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY data) AS pos
    FROM pedidos
)
SELECT cliente_id, valor FROM ordenado WHERE pos = 1;

-- 4
SELECT DISTINCT cliente_id FROM pedidos
WHERE data >= '2026-01-01' AND data < '2026-02-01'
EXCEPT
SELECT DISTINCT cliente_id FROM pedidos
WHERE data >= '2026-02-01' AND data < '2026-03-01';

-- 5
WITH mensal AS (
    SELECT DATE_TRUNC('month', data) AS mes, SUM(valor) AS total
    FROM pedidos GROUP BY 1
)
SELECT mes, total,
       ROUND(100.0 * (total - LAG(total) OVER (ORDER BY mes)) / LAG(total) OVER (ORDER BY mes), 2) AS variacao_pct
FROM mensal;
```
