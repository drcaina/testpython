print("DARWIN")
a = 5
b = 3
suma = a + b
print("La suma es:", suma)

# Buscar números primos en el rango del 1 al 50
print("Números primos del 1 al 50:")
for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
