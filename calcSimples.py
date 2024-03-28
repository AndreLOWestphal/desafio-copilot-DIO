
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

operacao = input("Digite qual operação deseja fazer (+,-,/,*): ")

if(operacao == "+"):
    print("A soma é: ", num1 + num2)
elif(operacao == "-"):
    print("A subtração é: ", num1 - num2)
elif(operacao == "/"):
    print("A divisão é: ", num1 / num2)
elif(operacao == "*"):
    print("A multiplicação é: ", num1 * num2)
else:print("Error")