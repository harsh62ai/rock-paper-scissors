import random
computer=random.randint(-1,1)
you=input("enter your choice: ")
d={"r":1,"p":0,"s":-1}
rd={1:"rock",0:"paper",-1:"scissors"}
you=d[you]
print(f"you choose {rd[you]}\n computer choose {rd[computer]}")
if(computer==you):
       print("its a tie")
elif(computer==1 and you==0 ):
       print("you won!")
elif(computer==1 and you==-1 ):
        print("you lose!")
elif(computer==0 and you==1):
        print("you lose!")
elif(computer==0 and you==-1 ):
        print("you won!")
elif(computer==-1 and you==1 ):
        print("you won!")
elif(computer==-1 and you==0 ):
        print("you lose!")