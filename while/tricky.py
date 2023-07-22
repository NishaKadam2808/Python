sum=0
while(True):
    p=int(input("Enter amount : "))
    sum=sum+p
    print("Total : ",sum)
    state=input("Do you want to continue : ")
    if(state=="no"):
        break
    
if(sum>=5000 and sum<=10000):
    print("Discount : ",sum*0.03)
    sum=sum-(sum*0.03)
    print("Discounted amount : ",sum)
if(sum>=10000 and sum<=15000):
    print("Discount : ",sum*0.05)
    sum=sum-(sum*0.05)
    print("Discounted amount : ",sum)
if(sum>=15000):
    print("Discount : ",sum*0.07)
    sum=sum-(sum*0.07)
    print("Discounted amount : ",sum)
