print("Olá, mundo!")

#----------------------------------------------------

def calcular_media(num1, num2, num3):
    return (num1 + num2 + num3) / 3

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    media = calcular_media(num1, num2, num3)
    print("A média dos três números é:", media)

if __name__ == "__main__":
    main()

#-----------------------------------------------------

def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            numero_palavras = len(palavras)
            return numero_palavras
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)
        return -1

def main():
    nome_arquivo = input("Digite o nome do arquivo de texto: ")
    numero_palavras = contar_palavras(nome_arquivo)
    if numero_palavras != -1:
        print("O arquivo", nome_arquivo, "contém", numero_palavras, "palavras.")

if __name__ == "__main__":
    main()

#----------------------------------------------------------

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    escolha = input("Escolha a conversão:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print("A temperatura em Fahrenheit é:", fahrenheit)
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print("A temperatura em Celsius é:", celsius)
    else:
        print("Escolha inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
 #----------------------------------------------------------

 import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'algoritmo', 'desenvolvimento']
    return random.choice(palavras)

def mostrar_palavra_secreta(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

def main():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")
    print(mostrar_palavra_secreta(palavra_secreta, letras_corretas))

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra.")
        elif letra in palavra_secreta:
            letras_corretas.append(letra)
            print("Boa! Essa letra está na palavra.")
        else:
            tentativas -= 1
            print("Essa letra não está na palavra. Você tem", tentativas, "tentativas restantes.")

        print(mostrar_palavra_secreta(palavra_secreta, letras_corretas))

        if '_' not in mostrar_palavra_secreta(palavra_secreta, letras_corretas):
            print("Parabéns! Você ganhou! A palavra secreta é:", palavra_secreta)
            break

    if tentativas == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

if __name__ == "__main__":
    main()

#-----------------------------------------------------------------

import os

def listar_arquivos_e_pastas():
    conteudo = os.listdir('.')
    for item in conteudo:
        print(item)

def main():
    print("Conteúdo do diretório atual:")
    listar_arquivos_e_pastas()

if __name__ == "__main__":
    main()
#------------------------------------------------------------------
def divisao(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        print("O resultado da divisão é:", resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

def main():
    dividendo = float(input("Digite o dividendo: "))
    divisor = float(input("Digite o divisor: "))
    divisao(dividendo, divisor)

if __name__ == "__main__":
    main()
#-----------------------------------------------------------------

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    else:
        return a / b

def main():
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número correspondente à operação desejada: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado da soma:", soma(num1, num2))
    elif escolha == '2':
        print("Resultado da subtração:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado da multiplicação:", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado da divisão:", divisao(num1, num2))
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------

import re

def validar_email(email):
    # Expressão regular para validar endereços de e-mail
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Verifica se o e-mail corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False

def main():
    email = input("Digite o endereço de e-mail a ser validado: ")
    if validar_email(email):
        print("O e-mail é válido.")
    else:
        print("O e-mail é inválido.")

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------

def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos_no_intervalo(inicio, fim):
    primos = []
    for numero in range(inicio, fim + 1):
        if verificar_primo(numero):
            primos.append(numero)
    return primos

def main():
    inicio = int(input("Digite o início do intervalo: "))
    fim = int(input("Digite o fim do intervalo: "))

    print(f"Números primos entre {inicio} e {fim}:")
    primos = encontrar_primos_no_intervalo(inicio, fim)
    for primo in primos:
        print(primo, end=" ")

if __name__ == "__main__":
    main()

