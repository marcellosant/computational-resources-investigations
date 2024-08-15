from math import factorial
import pandas as pd

# Valor da frequência que irá ser utilizado
VALOR_FREQUÊNCIA = 10 ** 9

def coluna_um():
    return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def coluna_dois(numeradores, denominadores):
    return [numerador / denominador for numerador, denominador in zip(numeradores, denominadores)]

def coluna_três(número_cidades):
    return [factorial(número - 1) for número in número_cidades]

def coluna_quatro(número_cidades):
    return [factorial(número - 1) / (VALOR_FREQUÊNCIA / (número - 1)) for número in número_cidades]

# Criar o DataFrame
dados = {
    'n': coluna_um(),
    'Rotas/s': coluna_dois(coluna_três(coluna_um()), coluna_quatro(coluna_um())),
    '(n-1)! = R(n) = Combinações': coluna_três(coluna_um()),
    'Tempo de Execução = TE = R(n) / (Rotas/s)': coluna_quatro(coluna_um())
}

# Criar o DataFrame do Pandas
df = pd.DataFrame(dados)

# Exibir o DataFrame
print(df)