planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]
planetaUser = input("Insira o nome do planeta (Com a primeira letra maiúscula, e com os acentos corretos.)")
userIndex = planetas.index(planetaUser)

print("Aqui estão os planetas mais próximos do sol comparados à: " + planetaUser)
print(planetas[0:userIndex])

print("E aqui vão os planetas mais longes do sol comparados à: " + planetaUser)
print(planetas[userIndex + 1:])