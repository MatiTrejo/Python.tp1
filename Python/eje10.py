numero = int(input("Introduce un número: "))
print(f"Los múltiplos de 3 menores a {numero} son:")

for i in range(3, numero, 3):
    print(i)
