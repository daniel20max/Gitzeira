nome = str(input("Seu Nome: "))
idade = int(input("Sua idade: "))
sexo = str(input("Sexo masc ou fem: "))
renda = int(input("Sua renda anual é: "))

if (renda == 0):
    print("Salario Invalido")
#Feminino.
if (sexo == "fem" and idade >= 61):
    print("Obrigado", nome, "Sua aposentadoria foi liberada no valor de: ", renda*0.7)
if (sexo == "fem" and idade <61):
    print("Falta um total de:", 61-idade,"para sua aposentadoria")
#Masculino.
if (sexo == "masc" and idade >= 66):
    print("Obrigado", nome, "Sua aposentadoria foi liberada no valor de: ", renda*0.75)
if (sexo == "masc" and idade <66):
    print("Falta um total de:", 66-idade,"para sua aposentadoria")
