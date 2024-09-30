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

#print(algoamais(2))    

def soma_dir_esq(k,n,a):
    if k > n:
        s = 0
    else: 
        s= a[k] + soma_dir_esq(k+1,n,a)
        return s     


        
        
def decide_i(A,n,x):
  i= 1
  A = list(range(1, n + 1)) 

  while i<=n and A[i] != x :
    i = i+1
  if i > n: return 'NAO'
  else: return 'SIM'

def decide_r(A,n,x):
  A = list(range(1, n + 1)) 

  if n==0:
    return "Não"   
  if A[n]==x:
    return "Sim"
  else: return  decide_r(A,n-1,x) 
A=[]
print(decide_i(A,10,10))


    
def f(n):
  if n == 0:
        return 10
    
  return f(n - 1) + n + 1

print(f(1000))



  
   
  