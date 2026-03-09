# definimos o dicionario (base de dados)

preco_frutas = {
    'maça': 2.5,
    'banana': 1.8,
    'laranja':3.0,
}

#Definimos qual a fruta queremos procurar 
frutas_desejada ='maça'

# fazemos a busca direta usando o método .get()
# O .get() tenta encontrar a fruta; se não achar mostra 'fruta não encontrada'
resultado =preco_frutas.get(frutas_desejada, 'fruta não encontrada')


# Exibimos o resultado 
print (f"o preço da {frutas_desejada} é R${resultado}")