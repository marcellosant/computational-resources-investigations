#Algo (n)
#1 se n = 0
#2 devolva 1
#3 x := Algo (n−1) + n + 1
#4 devolva x

def algo(n):
    if n == 0:
        return 1
    x = algo(n-1)+n+1
    return x

print(algo(3))
#Algo (n)
#1 se n = 0
#2 devolva 0
#3 x := Algo (n−1) + 2n − 1
#4 devolva x     

def algoamais(n):
    if n == 0:
        return 0
    x = algoamais(n-1)+2*n - 1
    return x

print(algoamais(2))    

def soma_dir_esq(k,n,a):
    if k > n:
        s = 0
    else: 
        s= a[k] + soma_dir_esq(k+1,n,a)
        return s     