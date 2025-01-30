"""
rock--1
paper--2
sissor--3
"""
import random 
a=True
while a==True:
    try:
        computer=random.choice([1,2,3])
        b=True
        while b==True:
            print("------------------")
            print("--rock,paper,sissor--GAME")
            print("------------------")
            youstr=str(input("enter your choice:"))
            print("------------------")
            if youstr=="rock" or youstr=="paper" or youstr=="sissor":
                b=False        
            else:
              print("??wrong input??\nplease input agian")

        dict1={1:"rock",2:"paper",3:"sissor"}
        print(f"your choice:{youstr}\ncomputer choice:{dict1[computer]}")
    except:
        print("there are some error")
        print("------------------")  
    dict2={"rock":1,"paper":2,"sissor":3}
    you=dict2[youstr]

    if dict1[computer]==youstr:
        print("!its a draw!")
        print("------------------")
    else:
        if computer==1 and you==2:
            print("!!you win!!")
            print("------------------")
        elif computer==1 and you==3:
            print("!!!you lose!!!")
            print("------------------")
        elif computer==2 and you==1:
            print("!!!you lose!!!")
            print("------------------")
        elif computer==2 and you==3:
            print("!!you win!!")
            print("------------------")
        elif computer==3 and you==1:
            print("!!you win!!")
            print("------------------")
        elif computer==3 and you==2:
            print("!!!you lose!!!")
            print("------------------")
        else:
            print("!!something went wrong!!")
            print("------------------")
        
    c=True
    while c==True:
        try:
            end=int(input("enter 4 for continue and 5 for end:"))
            print("------------------")
            if end==4 or end==5:
                c=False
            else:
                print("??wrong input??\nplease input agian")
                print("------------------")
        except:
            print("there is a error")
    if end==4:
        pass
    elif end==5:
        a=False
        print("!!!Thankyou for playing with me!!!")
        print("------------------")
    else:
        pass