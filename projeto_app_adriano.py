'''
CRUD



Açaiteria

Permitir que o cliente escolha, personalize e pague seu açaí pelo celular, 
com opção de entrega ou retirada.
Adriano
'''

print("\n=== AÇAÍTERIA ===")
print("1. Mais procurados")
print("2. Opções a deriva")
print("3. Montagem do proprio pedido")
print("4. Descontos e promoções")
print("5. Entregas (delivery)")
print("6. Redes sociais da empresa (meio de contato)")
print("0. Sair")


while True:
    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        print("Mais procurados...")
        print(" Açaí de 1L, Açaí de 300Ml, Açaí de 700Ml ")

    elif escolha == '2':
        print("Opções a deriva")
        print(" Açaí de copo, Marmita de açaí, Barca açaí ")

    elif escolha == '3':
        print("Montagem do propio pedido")
        print(" Escolher tamanho do açaí, Escolher extra, Escolher complementos ")

    elif escolha == '4':
        print("Descontos e promoções ")
        print(" Segunda do Açaí 20% de desconto em qualquer tamanho de açaí ")
        print(" Combo Amigos Compre 2 açaís grandes e ganhe 10% de desconto ")
        print("Monte Seu Açaí Na compra de um açaí médio ou grande, ganhe 1 adicional grátis")





else:
    print("Opção invalida. Por favor, tente novamente.")

