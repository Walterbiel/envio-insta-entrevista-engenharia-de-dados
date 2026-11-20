"""Teste prático de Python. Resolva as funções → rode o arquivo para conferir.
Gabarito no fim do arquivo (role só depois de tentar)."""


# 1. Retorne a lista sem duplicados, mantendo a ordem
def remover_duplicados(itens):
    pass


# 2. Agrupe e some: [("a", 1), ("b", 2), ("a", 3)] → {"a": 4, "b": 2}
def somar_por_chave(pares):
    pass


# 3. Achate uma lista de listas: [[1, 2], [3]] → [1, 2, 3]
def achatar(listas):
    pass


# 4. Divida a lista em lotes de tamanho n
def em_lotes(itens, n):
    pass


# 5. Retorne o primeiro caractere que não se repete na palavra, ou None
def primeiro_unico(texto):
    pass


if __name__ == "__main__":
    testes = [
        (remover_duplicados([3, 1, 3, 2, 1]), [3, 1, 2]),
        (somar_por_chave([("a", 1), ("b", 2), ("a", 3)]), {"a": 4, "b": 2}),
        (achatar([[1, 2], [3]]), [1, 2, 3]),
        (em_lotes([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
        (primeiro_unico("arara"), None),
        (primeiro_unico("dados"), "a"),
    ]
    for i, (veio, esperado) in enumerate(testes, start=1):
        print(f"Teste {i}:", "OK" if veio == esperado else f"ERRO → veio {veio!r}")


# GABARITO
#
# def remover_duplicados(itens):
#     return list(dict.fromkeys(itens))
#
# def somar_por_chave(pares):
#     total = {}
#     for chave, valor in pares:
#         total[chave] = total.get(chave, 0) + valor
#     return total
#
# def achatar(listas):
#     return [x for lista in listas for x in lista]
#
# def em_lotes(itens, n):
#     return [itens[i:i + n] for i in range(0, len(itens), n)]
#
# def primeiro_unico(texto):
#     from collections import Counter
#     contagem = Counter(texto)
#     return next((c for c in texto if contagem[c] == 1), None)
