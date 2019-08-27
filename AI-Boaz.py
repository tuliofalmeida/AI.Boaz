i = 1
print(" Talking to Boaz - SaguiEnglish v0.0.1")
while(i): 
    question = input("-Boaz says: Is it soinho or sagui? ")

    if (question == "soinho"):
        print("-Boaz says: You are right miseravi")
        i = 0
    elif (question == "sagui"):
        print("-Boaz says: Unpossible")
    elif (question == "brownie"):
            print("-Boaz says: 1 is 3, 2 is 5 ")
            sabor = input("-Boaz says: chocolate? ")
            quantidade = input("-Boaz says: quantos? ")
            if(sabor == "y" and int(quantidade) == 1):
                print("-Boaz says: 1 is 3 ")
            elif(sabor == "y" and int(quantidade) == 2):
                print("-Boaz says: 2 is 5 ")
            elif(sabor == "y" and int(quantidade) >3):
                print("-Boaz says: More than 3 is 10 percent out ")
            elif(sabor == "n"):
                print("-Boaz says: Not have and i'm not going to sell to you")
            else:
                print("-Boaz says: I don't understand, speak again")
            print("-Boaz says: But...")
    else:
        print("-Boaz says: You're worse than Augusto!")
        augusto = input("-Boaz says: Do you know Augusto?")
        if(augusto == "n"):
            resposta = input("-Boaz says: What you do for living?")
            print("-Boaz says: Augusto is better than you in " + resposta)
        elif(augusto == "y"):
            print("-Boaz says: Ask Augusto if... " )


'''botao1Apertado = float(input("O soinho apertou o botao1?"))
botao2Apertado = float(input("O soinho apertou o botao2?"))

if(not botao1Apertado and not botao2Apertado):
    print("O soinho mijou no botao")
if(botao1Apertado and not botao2Apertado):
    print("soinho tentou mijar em voce")
if(not botao1Apertado and botao2Apertado):
    print("soinho tentou mijar em voce")
if(botao1Apertado and botao2Apertado):
    print("soinho mijou em voce")
print("soinho fugiu")'''




