print("Olá, vamos calcular seu IMC, e pra isso irei precisar de algumas informações")
#
nome = input("Preciso que informe seu nome: ")
idade = input("Preciso que informe sua idade: ")
#
print("Muito bem " + nome + ", você tem " + idade + " anos de idade.")
#
peso = float(input("Agora iremos precisar do seu peso em KG: "))
altura = float(input("Agora iremos precisar da sua altura em metros: "))
#
imc = peso // (altura * altura)

def calcular_imc(peso, altura):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 29.9 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 34.9 <= imc < 39.9:
        return "Obesidade Grau 2"
    elif imc >= 39.9:
        return "Obesidade Grau 3"
    else:
        return "Valor de IMC inválido"
    
resultado = calcular_imc(peso, altura)

match resultado:
    case "Abaixo do peso":
        print(f"Sinto muito {nome}, informamos em dizer que você se encontra na categoria || {resultado} || ")
    case "Peso normal":
        print(f"Parabéns {nome}, informamos em dizer que você se encontra na categoria || {resultado} || ")
    case "Sobrepeso":
        print(f"Comeu demais hein {nome}, informamos em dizer que você se encontra na categoria || {resultado} || ")
    case "Obesidade Grau 1":
        print(f"Preocupante {nome}, informamos em dizer que você se encontra na categoria || {resultado} || ")
    case "Obesidade Grau 2":
        print(f"Muito preocupante {nome}, informamos em dizer que você se encontra na categoria || {resultado} || ") 
    case "Obesidade Grau 3":
        print(f"É fã da Thais Carla {nome}? Informamos em dizer que você se encontra na categoria || {resultado} || ") 

print("Quer ler é gay")