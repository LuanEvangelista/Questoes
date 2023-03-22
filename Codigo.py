# Questao 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
#resposta 91

# Questao 2

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

num = int(input("Digite um número: "))

fib_seq = [0, 1]
while fib_seq[-1] < num:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

if num in fib_seq:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

# Questao 3
''' 3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, 9 - já que a sequência está aumentando de 2 em 2.

b) 2, 4, 8, 16, 32, 64, 128 - já que a sequência está dobrando a cada termo.

c) 0, 1, 4, 9, 16, 25, 36, 49 - já que a sequência está adicionando os números ímpares em ordem crescente.

d) 4, 16, 36, 64, 100 - já que a sequência está aumentando de 12 em 12.

e) 1, 1, 2, 3, 5, 8, 13 - já que a sequência é a sequência de Fibonacci.

f) 2,10, 12, 16, 17, 18, 19, 20 - já que a sequência está aumentando em valores irregulares pois nao é Matematica convencional.
porem pode ser uma sequencia especifica : 
2 (two) = 3 caracteres
10 (ten) = 3 caracteres
12 (twelve) = 6 caracteres
16 (sixteen) = 7 caracteres
17 (seventeen) = 9 caracteres
18 (eighteen) = 8 caracteres
19 (nineteen) = 8 caracteres
20 (twenty) = 6 caracteres

'''

# Questao 4

''' 
podemos utilizar a fórmula de distância, que relaciona distância, velocidade e tempo:

distância = velocidade x tempo

Vamos começar calculando o tempo que cada veículo leva para chegar ao ponto de cruzamento:

Tempo do carro = distância / velocidade = 100 / 110 = 0.91 horas

Tempo do caminhão = distância / velocidade = 100 / 80 = 1.25 horas

No entanto, sabemos que o caminhão precisa passar por 2 pedágios, o que adiciona um tempo extra de 5 minutos (ou 1/12 de hora) para cada um. Portanto, o tempo total do caminhão será:

Tempo total do caminhão = 1.25 + 1/6 = 1.4167 horas

Agora que sabemos os tempos de cada veículo, podemos calcular a distância percorrida por cada um até o ponto de cruzamento:

Distância percorrida pelo carro = 0.91 x 110 = 100.1 km

Distância percorrida pelo caminhão = 1.4167 x 80 = 113.3 km

Portanto, podemos concluir que o carro estará mais próximo da cidade de Ribeirão Preto no ponto de cruzamento, já que percorreu uma distância menor do que o caminhão. 
É importante notar que o fato do carro ter um sistema de pedágio mais eficiente não influenciou diretamente na resposta, 
já que a diferença na distância percorrida foi maior do que a diferença de tempo por conta dos pedágios.

'''

# Questao 5

string = "exemplo de string para inverter"

lista_caracteres = list(string)

tamanho_lista = len(lista_caracteres)

for i in range(tamanho_lista // 2):
    lista_caracteres[i], lista_caracteres[tamanho_lista - i - 1] = lista_caracteres[tamanho_lista - i - 1], lista_caracteres[i]

string_invertida = "".join(lista_caracteres)

print(string_invertida)
