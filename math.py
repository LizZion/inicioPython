planeta1 = int(input("Insira a distância entre o primeiro planeta e o sol."))
planeta2 = int(input("Insira a distância entre o segundo planeta e o sol."))

distkm = planeta1 - planeta2
print("Distância (KM): " + str(abs(distkm)))

distmi = distkm / 1.609344
print("Distância (Milhas): " + str(abs(distmi)))