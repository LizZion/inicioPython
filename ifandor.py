tam_obj = int(input("Tamanho do objeto: "))
prox = int(input("Proximidade do objeto: "))

if tam_obj > 5 and prox < 1000:
    print('ALERTA: Manobras evasivas necessárias!')
else:
    print('ALERTA: Objetos próximos sem nenhum problema.')