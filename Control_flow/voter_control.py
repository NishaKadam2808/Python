age=int(input("Enter age : "))
if(age>=18):
    print("Eligible to Vote...")
    gender=input("Enter gender : ")
    if(gender=='male'):
        print("Vote on 1st booth..")
        if(age>70):
            print("Senior citizen...")
        else :
            print("Junior citizen..")
    elif(gender=='female'):
        print("Vote on 2nd booth..")
        if(age>70):
            print("Senior citizen...")
        else :
            print("Junior citizen..")
    else:
        print("Invalid..")
else:
    print("Can't vote..")
    
