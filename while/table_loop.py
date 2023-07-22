#total percentage form user subs using while
total=0
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
    print("E")

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
