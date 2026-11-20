# Entrevista de Engenharia de Dados

Material gratuito do QG da Engenharia de Dados. Você recebeu porque comentou **ENTREVISTA**.

60 perguntas que caem em entrevista, com respostas curtas.

## Como usar este material

1. Leia a pergunta → tente responder em voz alta **antes** de ler a resposta
2. Marque as que errou → estude e volte depois
3. Faça os testes práticos em [testes](testes) → gabarito no mesmo arquivo, no fim

## Fundamentos

**1. O que faz um engenheiro de dados?**
Constrói e mantém os pipelines que levam o dado da origem até quem usa, com qualidade e no prazo.

**2. ETL x ELT?**
ETL transforma antes de carregar. ELT carrega cru e transforma dentro do destino.

**3. Batch x streaming?**
Batch processa blocos de tempos em tempos. Streaming processa cada evento quando chega.

**4. OLTP x OLAP?**
OLTP atende o sistema (muitas escritas pequenas). OLAP atende análise (leituras grandes).

**5. Data lake x data warehouse?**
Lake guarda qualquer formato barato. Warehouse guarda dado estruturado pronto para consulta.

**6. O que é Lakehouse?**
Data lake com uma camada de tabela (Delta, Iceberg) que dá transação, versão e SQL.

**7. O que é arquitetura Medallion?**
Camadas bronze (cru), silver (limpo) e gold (regra de negócio).

**8. O que é idempotência?**
Rodar o pipeline várias vezes gera o mesmo resultado. Evita duplicar dado em reprocesso.

**9. O que é backfill?**
Reprocessar períodos passados, por exemplo depois de corrigir uma regra.

**10. O que é data lineage?**
O caminho que o dado fez: de onde veio e por quais transformações passou.

## SQL

**11. WHERE x HAVING?**
WHERE filtra linhas antes do agrupamento. HAVING filtra grupos depois.

**12. Tipos de JOIN?**
INNER (só pares), LEFT (tudo da esquerda), RIGHT (tudo da direita), FULL (tudo dos dois).

**13. UNION x UNION ALL?**
UNION remove duplicados. UNION ALL mantém tudo e é mais rápido.

**14. O que é window function?**
Cálculo sobre um conjunto de linhas sem agrupar, usando OVER().

**15. ROW_NUMBER x RANK x DENSE_RANK?**
Empate: ROW_NUMBER não repete, RANK repete e pula, DENSE_RANK repete e não pula.

**16. Como remover duplicados mantendo o mais recente?**
ROW_NUMBER() OVER (PARTITION BY chave ORDER BY data DESC) e filtrar = 1.

**17. O que é CTE?**
Consulta nomeada com WITH, para deixar SQL complexo legível.

**18. O que é um índice?**
Estrutura que acelera a busca em uma coluna, com custo na escrita.

**19. Normalização?**
Organizar tabelas para evitar repetição e inconsistência (1FN, 2FN, 3FN).

**20. Como otimizar uma consulta lenta?**
Ver o plano (EXPLAIN), filtrar cedo, evitar SELECT *, criar índice ou particionar.

## Modelagem

**21. Fato x dimensão?**
Fato guarda eventos e números. Dimensão guarda o contexto (quem, onde, quando).

**22. Star x snowflake?**
Star tem dimensões desnormalizadas. Snowflake quebra dimensões em mais tabelas.

**23. O que é granularidade?**
O que uma linha da fato representa. Ex: 1 linha por item vendido.

**24. O que é chave surrogate?**
Chave artificial do DW, independente da chave do sistema de origem.

**25. O que é SCD tipo 2?**
Guarda histórico criando uma nova linha a cada mudança, com datas de vigência.

## Python

**26. Lista x tupla?**
Lista é mutável. Tupla é imutável.

**27. O que é generator?**
Função com yield que entrega um item por vez, sem carregar tudo na memória.

**28. O que é decorator?**
Função que envolve outra para adicionar comportamento (log, retry, tempo).

**29. Como ler um arquivo grande no pandas?**
Em pedaços com chunksize, só as colunas necessárias, ou trocar por Polars ou DuckDB.

**30. Como guardar senha no código?**
Não guarda. Usa variável de ambiente ou cofre de segredos.

## Ferramentas

**31. O que é Airflow?**
Orquestrador: agenda e monitora pipelines definidos como DAGs em Python.

**32. O que é uma DAG?**
Grafo de tarefas com dependências e sem ciclos.

**33. O que é dbt?**
Ferramenta que transforma dados com SQL dentro do warehouse, com testes e documentação.

**34. O que é Spark?**
Motor de processamento distribuído para grandes volumes.

**35. Transformação x ação no Spark?**
Transformação é preguiçosa (monta o plano). Ação executa (count, write, show).

**36. O que é partição?**
Divisão do dado (por data, por exemplo) para ler só o necessário.

**37. O que é Kafka?**
Plataforma de streaming que guarda eventos em tópicos e entrega para consumidores.

**38. Tópico, partição e consumer group?**
Tópico é a fila lógica, partição divide o tópico para paralelismo, grupo divide as partições entre consumidores.

**39. Por que Docker em dados?**
Mesmo ambiente na máquina, no teste e em produção.

**40. Por que Parquet?**
Formato colunar e comprimido: lê só as colunas necessárias e ocupa menos espaço.

## Cloud e arquitetura

**41. Arquitetura Lambda?**
Batch e tempo real em paralelo, juntos na camada de serving.

**42. Arquitetura Kappa?**
Tudo como streaming; reprocessar é reler o log.

**43. O que é Data Mesh?**
Organização em que cada domínio é dono dos seus dados como produto.

**44. O que é CDC?**
Capturar só as mudanças da origem (insert, update, delete).

**45. Como controlar custo na nuvem?**
Desligar o que não usa, particionar, escolher o tamanho certo do cluster e monitorar.

**46. O que é IaC?**
Infraestrutura criada por código (Terraform), versionada e repetível.

**47. O que é CI/CD em dados?**
Testar e publicar pipelines automaticamente a cada mudança no repositório.

**48. Como garantir qualidade de dados?**
Testes de nulos, unicidade, integridade e regras de negócio em cada camada.

**49. O que é observabilidade de dados?**
Monitorar volume, atraso, esquema e qualidade para saber de problemas antes do usuário.

**50. O que é governança?**
Regras de acesso, catálogo, dono do dado e conformidade com LGPD.

## Comportamental e cenários

**51. Um pipeline falhou de madrugada. O que você faz?**
Vejo o log, avalio impacto, comunico, corrijo, reprocesso e registro a causa.

**52. O dashboard mostra número errado. Como investiga?**
Volto camada por camada (gold → silver → bronze → origem) até achar onde diverge.

**53. Como você prioriza demandas?**
Pelo impacto no negócio e pelo esforço, alinhando com quem pediu.

**54. Fale de um projeto seu.**
Problema → arquitetura → ferramentas → resultado em número.

**55. Como explicar algo técnico para alguém de negócio?**
Começo pelo impacto, uso exemplo do dia a dia, evito jargão.

**56. A origem mudou o esquema sem avisar. E agora?**
Teste de esquema no pipeline, alerta, ajuste e conversa com o time dono da origem.

**57. Como você versiona o seu trabalho?**
Git com branch por mudança e pull request revisado.

**58. Batch diário está demorando demais. O que faz?**
Mudo para carga incremental, particiono e reviso as consultas mais pesadas.

**59. Por que engenharia de dados?**
Resposta pessoal: conecte com resolver problemas reais com dados.

**60. Tem alguma pergunta para nós?**
Sempre tenha: como é a stack, como é o time, quais os maiores desafios de dados hoje.

## QG da Engenharia de Dados

Este material é uma amostra do que você encontra no QG.

→ Trilha completa do zero ao sênior
→ Projetos reais para o portfólio
→ Comunidade para tirar dúvidas

Acesse → [qg-engenharia-de-dados.com.br](https://qg-engenharia-de-dados.com.br)
YouTube → [@gonzagadosdados](https://www.youtube.com/@gonzagadosdados)
