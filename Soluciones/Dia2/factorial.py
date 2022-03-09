numero = int(input("Ingresa tu numero: "))

res = 1
for i in range(numero):
  res = (i+1)*res
print("El factorial de ", numero, " es ", res)