import random
def game(you):
   computer=random.randint(1,3)
   print("computer choose {computer}")
   d={1:"rock",2:"paper",3:"scissors"}
   you=input(print("give your choice:"))
   yourdict ={"rock":1,"paper":2,"scissors":3}
   print("you choose{yourdict [you] }/n computer choose{d[computer]}")
   if(computer==you):
       print("its a tie")
   elif(computer==1 and you==2 ):
       print("you won!")
   elif(computer==1 and you==3 ):
        print("you loose!")
   elif(computer==2 and you==1):
        print("you loose!")
   elif(computer==2 and you==3 ):
        print("you won!")
   elif(computer==3 and you==1 ):
        print("you won!")
   elif(computer==3 and you==2 ):
        print("you loose!")
 
game(1)

     




