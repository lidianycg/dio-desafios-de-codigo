valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

# Inicializa a variável valor_final com o mesmo valor que foi inserido em valor_inicial.
valor_final = valor_inicial

# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    return valor_inicial * (1 + taxa_juros)**periodo

# Chama a função e atribui o resultado à variável valor_final
valor_final = calcular_valor_final(valor_inicial, taxa_juros, periodo)

valor_final_formatado = "{:.2f}".format(valor_final)
print("Valor final do investimento: R$", valor_final_formatado)