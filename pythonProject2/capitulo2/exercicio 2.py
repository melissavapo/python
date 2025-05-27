precoCapaLivro = 24.95
precoCapaLivroDesconto = precoCapaLivro - (precoCapaLivro * 0.40)
custoFretePrimeiroExemplar = precoCapaLivroDesconto + 3.00
custoFreteRestateExemplares =  precoCapaLivroDesconto + 0.75
custoTotalAtacado = custoFretePrimeiroExemplar + (custoFreteRestateExemplares * 59)

print("o preco total de atacado para 60  exemplares é de:" , custoTotalAtacado)