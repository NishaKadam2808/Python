#total percentage form user subs using while
'''total=0
i=0
while(i<5):
    m=int(input("Enter marks : "))
    total=total+m
    i=i+1
per=total/5
print("Total : ",total)
print("Per : ",per)
if(per>90 and per<=100):
    print("A")
elif(per>80 and per<=90):
    print("B")
elif(per>70 and per<=80):
    print("C")
elif(per>60 and per<=70):
    print("D")
elif(per>0 and per<=60):
    print("E")'''

#1 no table
'''n=int(input("Enter number : "))
i=1
while(i<=10):
    m=i*n
    print(m)
    i=i+1'''

#multiple no table
'''i=1
while(i<=10):
    print("Table of : ",i)
    j=1
    while(j<=10):
        print(i*j,end=' ')
        j=j+1
    print()
    i=i+1'''

#multiple no table from user range
'''i=int(input("Enter start : "))
a=int(input("Enter end : "))
while(i<=a):
    print("Table of : ",i)
    j=1
    while(j<=10):
        print(i*j,end=' ')
        j=j+1
    print()
    i=i+1'''

#sum of list
'''x=[5,6,7,[10,15,16,19],(20,25),30]
i=0
sum=0
while(i<len(x)):
    if(type(x[i])==list or type(x[i])==tuple):
        j=0
        while(j<len(x[i])):
            sum=sum+x[i][j]
            j=j+1
    else:
        sum=sum+x[i]
    i=i+1
print("Sum : ",sum)'''

#percentage and marks of nested list 
'''x=[[90,30,40,50,70],[100,40,40,50,70],[90,70,100,50,70],[40,30,40,100,70]]
i=0
sum=0
while(i<len(x)):
    j=0
    sum=0
    while(j<len(x[i])):
        sum=sum+x[i][j]
        j=j+1
    print("Sum of ",i,"list :",sum)
    print("Per of ",i,"list :",sum/5)
    if((sum/5)>40 and (sum/5)<=50):
        print("Pass")
    elif((sum/5)>50 and (sum/5)<=60):
        print("2nd class")
    elif((sum/5)>60 and (sum/5)<=75):
        print("1st class")
    elif((sum/5)>75 and (sum/5)<=100):
        print("Distinction")
    else:
        print("Fail")
    i=i+1'''

#prime using while
'''x=int(input("Enter no. : "))
i=2
flag=0
while(i<x):
    if(x%i==0):
        flag=1
        break
    i=i+1
if(flag==1):
    print("not Prime")
else:
    print(" prime")'''


no=0
while(no<100):
    no=no+1
    i=2
    flag=0
    while(i<no):
        if(no%i==0):
            flag=1
        i=i+1
    if(flag==0):
        print(no)
'''if(flag==1):
    print("not Prime")
else:
    print(" prime")'''


        
