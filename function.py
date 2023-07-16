#Function
'''Function is a block of statements that reduce length and execution time of program'''

#function ex.
'''def add():
    a=10
    b=20
    print(a+b)
add()'''

'''def sub():
    a=70
    b=20
    print(a-b)
sub()'''

'''def c():
    global a
    b=30
    print(a+b)
a=30
c()
print(a+b)'''


#find palindrome word from sentence
'''def palindrome(x):
    v=x.split()
    for i in v:
        z=i[::-1]
        if(i==z and len(i)>1):
            print(i)
palindrome('I repaper my mobiles rotator')'''

#prime and super prime (Ex.31)
'''no=int(input())
def prime(no):
    for i in range(2,no):
        if(no%i==0):
            return False
        else:
            return True
x=prime(no)
if(x==True):
    print("prime")
    if(no>9):
        sum=0
        for i in str(no):
            sum=sum+int(i)
            x=prime(sum)
            if(x==True):
                print("Super prime")
else:
    prime("Not prime")'''


            
