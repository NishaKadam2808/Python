#slicing in string
'''x='i love karad'
print(x[2:6])'''

#changing not possible
'''x='i love karad'
x[0]='u'
print(x)'''

#string methods
'''x='i love karad'
y='I LOVE KARAD'
print(x.upper())
print(y.lower())
print(x.title())
print(x.index('love'))
print(x.find('love'))
print(x.replace('karad','india'))
print(x)
print(x.split())
print(y.center(20,'*'))
print(y.islower())
print(x.isupper())
print(x.zfill(4))
print(x+y) #concate
print(x.rindex('i'))
print(" ",x*3," ")'''





#lower without method
''''x='i love karad'
for i in x:
    if(ord(i)>=97 and ord(i)<=122):
        print(chr(ord(i)-32),end='')
    else:
        print(i,end=' ')'''

#upper without method
'''x='I LOVE KARAD'
for i in x:
    if(ord(i)>=33 and ord(i)<=126):
        print(chr(ord(i)+32),end='')
    else:
        print(i,end='')'''

#upper first letter without using title
'''x='i love karad'
y=x.split()
for j in y:
    for i in range(len(j)):
        if(i==0):
            a=ord(j[i])
            print(chr(a-32),end='')
        else:
            print(j[i],end='')
    print(' ',end='')'''


'''x='aBcrp2@4$XyQ4b-'
c=''
s=''
n=''
sy=''
for i in x:
    if(ord(i)>=65 and ord(i)<=90):
        c=c+i
    elif(ord(i)>=97 and ord(i)<=122):
        s=s+i
    elif(ord(i)>=48 and ord(i)<=57):
        n=n+i
    elif((ord(i)>=91 and ord(i)<=96) or (ord(i)>=58 and ord(i)<=64) or (ord(i)>=32 and ord(i)<=47)):
        sy=sy+i
print(c+s+n+sy)'''

#password validation
'''password=input("Enter password : ")
flag1=0
flag2=0
flag3=0
flag4=0
flag5=0
if(len(password)>=8):
    for i in password :
        if((ord(i)>=65 and ord(i)<=90)):
            flag2=1
        elif((ord(i)>=97 and ord(i)<=122)):
            flag3=1
        elif((ord(i)>=48 and ord(i)<=57)):
            flag4=1
        elif(((ord(i)>=91 and ord(i)<=96) or (ord(i)>=58 and ord(i)<=64) or (ord(i)>=32 and ord(i)<=47))):
            flag5=1
if(flag2==1 and flag3==1 and flag4==1 and flag5==1 ):
    print("Valid")
else:
    print("invalid")'''












import time
p='Nisha@12'
flag=0
while(True):
    time.sleep(2)
    for i in range(3):
        a=input("Enter password : ")
        if(a==p):
            flag=flag+1
    if(flag==3):
        print("Login Successfull")
    else:
        print("Logout")
        s=input("Do you want to continue :")
        if(s=='no'):
            break
    
    
        
































        
        
        
        


        
    
        
