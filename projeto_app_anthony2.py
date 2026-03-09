'''
CRUD

Açaiteria

Permitir que o cliente escolha e persionalize seu pedido e pague seu açaí
pelo celular, com opção de entrega ou retirada.
'''

print("\n=== AÇAÍTERIA ===")
print("1. Mais procurados")
print("2. Opções a deriva")
print("3. Montagem do propio pedido")
print("4. Descontos e promoções")
print("5. Entregas (Delivery)")
print("6. Redes socias da empresa")
print("0. Sair")



while True:
    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
     print("Mais procurados...")
    # Código para mais procurados 

    elif escolha == '2' : 
       print("Opções a deriva")
    elif escolha == '3' :
       print("Montagem do propio pedido")
    elif escolha == '4' :
       print("Descontos e promoções ")
    elif escolha == '5' :
       print("Entregas (delivery)")
    elif escolha == '6' :
       print("Redes sociais da empresa")
    elif escolha == '0':
       print("Saindo do sistema")
    break



else:
    print("Opção inválida. Por favor, tente novamente.")

 