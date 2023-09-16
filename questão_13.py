print("\n....Calculadora de peso ideal....\n")

altura = float(input("Qual sua altura em metros? "))
genero = input("\nVocê é um homem ou mulher? ")

if genero == "homem":
    peso_ideal = (72.7*altura)-58

if genero == "mulher": 
    peso_ideal = (62.1*altura)-44.7

else:
    print("Genêro inválido!")

print("Seu peso ideal é: ", peso_ideal)