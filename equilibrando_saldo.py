saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())


saldo_atual += valor_deposito
saldo_atual -= valor_retirada


saldo_final_formatado = "{:.1f}".format(saldo_atual)
print("Saldo atualizado na conta:", saldo_final_formatado)