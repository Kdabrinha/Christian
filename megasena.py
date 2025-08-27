import random


nu = list(range(1, 61))  # números de 1 a 60

# sorteio de 6 números sem repetição
sorteados = random.sample(nu, 6)

# organizar em ordem crescente
sorteados.sort()

# mostrar resultado
print("Números sorteados da Mega-Sena:")
print(sorteados)