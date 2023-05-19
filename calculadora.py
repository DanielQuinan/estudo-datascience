

def inicio():
    print("Calculadora Python")
    print("Selecione o número da operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    selecao = input("Escolha a função: ")
    selecionarcalculo(selecao)

def selecionarcalculo(selecao):
    if selecao == "1": 
        print("Você escolheu soma")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma(num1, num2)
    elif selecao == "2": 
        print("Você escolheu subtração")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        subtracao(num1, num2)
    elif selecao == "3": 
        print("Você escolheu multiplicação")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        multiplicacao(num1, num2)
    elif selecao == "4": 
        print("Você escolheu divisão")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        divisao(num1, num2)
    else:
        selecaoincorreta = input("Escolha uma alternativa correta: ")
        selecionarcalculo(selecaoincorreta)

def repetirprograma():
    repetir = input("Deseja voltar ao início?(Y/N)")
    if repetir.lower() == "y":
        inicio()
    elif repetir.lower() == "n":
        return print("Fim do Programa")
    else:
        print("Escolha uma opção correta")
        repetirprograma()
        
def soma(num1, num2):
    print(num1 + num2)
    repetirprograma()
def subtracao(num1, num2):
    print(num1 - num2)
    repetirprograma()
def multiplicacao(num1, num2):
    print(num1 * num2)
    repetirprograma()
def divisao(num1, num2):
    print(num1 / num2)
    repetirprograma()

inicio()