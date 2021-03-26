n1 = int(input("Digite o primeiro numero:\n"))
n2 = int(input("Digite o segundo numero:\n"))
op = str(input("informe o sinal - ou +:\n"))

resultado=("");
if (op == "-"):
    resultado=(n1 - n2)
if (op == "+"):
    resultado=(n1 + n2)
if (op != "-" and op != "+"):
    resultado= "Falha na operação"
if (resultado < 0 or resultado == 0 ):
    print("Se liga no resultado", resultado)
if not (resultado < 0  or resultado == 0):
    print("O resultado foi", resultado)
print("O Resultado do Calculo é:", resultado)
