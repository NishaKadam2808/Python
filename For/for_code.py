#for loop
'''x=[10,20,30,True,'Nisha',3.11,"India"]
for i in x:
    print(i)'''

#sum of ele in lst using for
'''x=[98,99,97,99,96]
sum=0
for i in x:
    sum=sum+i
print(sum)
print(sum/5)
if((sum/5)>40 and (sum/5)<=50):
    print("Pass")
elif((sum/5)>50 and (sum/5)<=60):
    print("2nd class")
elif((sum/5)>60 and (sum/5)<=75):
    print("1st class")
elif((sum/5)>75 and (sum/5)<=100):
    print("Distinction")
else:
    print("Fail")'''

#odd even ele sum
'''x=[7,9,10,13,16,20,21,35]
sum1=0
sum2=0
for i in x:
    if(i%2==0):
        print(i," even")
        sum1=sum1+i
    else:
        print(i," odd")
        sum2=sum2+i
print("Even sum : ",sum1)
print("Odd sum : ",sum2)'''

#printing no using range without taking list
'''for i in range(30):
    print(i)'''

#printing even odd from range
'''for i in range(30):
    if(i%2==0):
        print(i," : even")
    else:
        print(i," : odd")'''

#print from 1 to anther no. range
'''for i in range(0,10,2):
    print(i)'''

#prime using for
'''no=int(input("Enter no : "))
flag=0
for i in range(2,no):
    if(no%i==0):
        flag=1
        break
if(flag==1):
    print("Not prime")
else:
    print("Prime")'''

#table of range
'''s=int(input("Enter start : "))
e=int(input("Enter end : "))
for i in range(s,e+1):
    for j in range(1,11):
        print(i*j,end=' ')
    print()'''

#reverse print using for
'''for i in range(100,-1,-1):
    print(i)'''

#largest using for
'''x=[7,9,10,13,16,20,21,35]
m=x[0]
for i in x:
    if(i<m):
        m=i
print(m)'''

#sum of nested list
'''x=[30,10,[70,90,52],45,22,(30,35,70),75]
sum=0
for i in x:
    if(type(i)==list or type(i)==tuple):
        for j in i:
            sum=sum+j
    else:
        sum=sum+i
print(sum)'''

#per and sum of nested list and finding atkt and fail
'''marks=[[70,75,68,62,60],[48,49,30,58,62],[32,28,62,30,58],[68,75,78,79,65],[70,72,69,28,70]]
sum=0
flag=0
for i in marks:
    if(type(i)==list):
        sum=0
        for j in i:
            sum=sum+j
            if(j<40):
                flag=flag+1  
        print("Total of list ",i,":",sum)
        print("Per of list ",i,":",sum/5)
        if(flag==1 or flag==2):
            print("ATKT")
        elif(flag>=3):
            print("Fail")
        elif(sum/5>60 and sum/5<=70):
            print("Pass")
        elif(sum/5>70 and sum/5<=80):
            print("2nd Class")
        elif(sum/5>80 and sum/5<=90):
            print("1st class")
        elif(sum/5>90 and sum/5<=100):
            print("Distinction")'''

'''while(True):
    print("gg")'''

'''d={1:40,2:50,3:70,4:75,5:80}
for i in d:
    print(i,d[i])'''


d={1:40,2:50,3:70,4:75,5:80}
for i,j in d.items():
    print(i,j)






















