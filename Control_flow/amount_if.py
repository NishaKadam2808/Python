amount=int(input("Enter amount : "))
gst=amount*0.18
amount=amount+gst
if(amount<1000):
    dis=amount
    print(" no Discount : ")
    amount=amount-dis
    print("Amount with ",gst," GST: ",amount)
if(amount>=1000 and amount<=1500):
    dis=amount*0.02
    print(" 2% Discount : ",dis)
    amount=amount-dis
    print("Amount with ",gst,"GST and 2% discount : ",amount)
elif(amount>=1500 and amount<=2000):
    dis=amount*0.03
    print(" 3% Discount : ",dis)
    amount=amount-dis
    print("Amount with ",gst," GST: ",amount)
elif(amount>=2000 and amount<=3000):
    dis=amount*0.04
    print(" 4% Discount : ",dis)
    amount=amount-dis
    print("Amount with ",gst,"GST : ",amount)
elif(amount>=3000):
    dis=amount*0.05
    print(" 5% Discount : ",dis)
    amount=amount-dis
    print("Amount with ",gst," GST: ",amount)

    
    
