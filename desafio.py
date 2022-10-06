resultado = [5, 17, 1, 22, 29, 21]

aposta = []

contador = 0

for cont in range(1,7):
    aposta.append(int(input("Digite seu primeiro número: ")))

for comp1 in resultado:
    for comp2 in aposta:
        if(comp1 == comp2):
            contador += 1

print(resultado)

print(aposta)

print(contador)