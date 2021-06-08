sigue = ""
while sigue!= "n" or sigue!="s":
    sigue= input("quiere volver a jugar(s/n): ")
    if sigue == "n":
        jugando = false
        break
    elif sigue == "s":
        break
    else:
        print ("No te he entendido") 
