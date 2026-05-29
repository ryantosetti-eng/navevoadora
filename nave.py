combustivel = 110
tripulantes = []

def viajar():
    global combustivel
    if(combustivel>=30):
       combustivel = combustivel - 30
       print("A nave viajou")
    else:
       print("Voce esta sem combustivel suficiente. Abastesça!")

def abastecer():
   global combustivel
   combustivel = 100
   print("Taque cheio ⛽ ")

def status_nave():
     print("------Status da nave-----")
     print(f"Temos{combustivel} de combustivel")
     print(f"Os tripulantes sao: {tripulantes}")
     print("-------------------------------\n")

def registrartripulante():
    novotripulante = input("Qual o nome do novo tripulante?:")
    tripulantes.append(novotripulante)
    print("Tripulante inserido com sucesso🚀")

while True:
    print("\n Bem vindo ao menu interativo da nave. por favor selecione uma opçao:")
    print("\n1- Mostrar status da nave | 2-Viajar | 3-Abastecer | 4- Novo Tripulante | 5-Sair")
    opçao = input("Escolha:")
    if(opçao =="1"):
     status_nave()
    elif(opçao == "2"):
     viajar()
    elif(opçao == "3"):
     abastecer()
    elif(opçao == "4"):
       registrartripulante()
    elif(opçao == "5"):
       print("Viajem encerrada!")
       break
       

     
#status_nave()
#registrartripulante()
#status_nave()
   
    
#status_nave()
#viajar();
#viajar();
#status_nave()
#viajar();
#abastecer()
#viajar()
#status_nave()
