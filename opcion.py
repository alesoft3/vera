seguir = ""
while seguir!= "n" or seguir!="s":
    seguir= input("quiere volver a jugar(s/n): ")
    if seguir == "n":
        jugando = false
        break
    elif seguir == "s":
        break
    else:
        print ("No te he entendido") 
