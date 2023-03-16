planeta_novo = ''
planetas = []

while planeta_novo.lower() != 'fim':
    if planeta_novo:
        planetas.append(planeta_novo)
    planeta_novo = input('Insira um novo planeta, ou "fim" se acabou. ')

for planeta in planetas:
    print(planeta)

print("Todos os planetas são: " + str(planetas))