def fib(x):
    if (x == 0) or (x == 1):
        return x
    return fib(x-2) + fib(x-1)


for i in range (1,40):
    print(fib(i))


 
def fib_i(n):
    atual = 0
    ultimo = 1
    penultimo = 0

    for i in range(1, n + 1):
        if i == 1:
            atual = penultimo
        elif i == 2:
            atual = ultimo
        else:
            atual = ultimo + penultimo
            penultimo = ultimo
            ultimo = atual

    return atual
  


print(fib_i(2))
print(fib(2))