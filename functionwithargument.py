#simple add
'''def add(a,b):
    return a+b
print(add(30,20))'''

#sum of list ele usong function
'''def marks(a):
    sum=0
    i=0
    while(i<len(a)):
        sum=sum+a[i]
        i=i+1
    print(sum)
m=[90,80,70,72,65]
marks(m)'''

#function with fixed arg.
'''def person(name,age=17):
    print(name,age)
person("NK",100)
person("Nisha")'''


#nested list add(function with infinite arg.)
'''def add(*a):
    print(a)
    i=0
    sum=0
    for i in a:
        if(type(i)==list or type(i)==tuple):
            for j in i:
                if(type(j)==list or type(j)==tuple):
                    for k in j:
                        sum=sum+k
                else:
                    sum=sum+j
        else:
            sum=sum+i
       
    print(sum)
add([20,30,40],[50,70,(90,50,54,72,79),55,45],50,70)'''







#hw1
'''def marks(*a):
    print(a)
    sum=0
    for i in a:
        sum=0
        if(type(i)==list):
            for j in i:
                sum=sum+j
        print("Sum of ",i, ":",sum)
        print("percentage : ",(sum/5))
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
marks([50,25,30,55,22],[56,90,23,22,11],[99,96,90,91,92],[78,88,89,67,10],[97,96,93,94,92],[91,96,95,96,98])'''










#function with infinite arg.
'''def person(**a):
    for i in a:
        
        print(i,":",a[i])
        print("\n")
        
person(name="Nisha",company="Amplifier",desig="Engineer",phno=9876543210,city="karad",pincode=415124)'''

'''def marks(**a):
    sum=0
    for  i in a:
        sum=0
        if(type(a[i])==list):
            for j in a[i]:
                sum=sum+j
                print(sum)'''
        


'''def marks(**a):
    t_m=0
    max_i=0
    sum=0
    for i in a:
        t_m=sum
        sum=0
        if(type(a[i])==list):
            for j in a[i]:
                sum=sum+j
                if(sum>t_m):
                    max_i=i
                    mx=sum
            
        print("Sum of ",i,"Marks :",sum)
        print("percentage of ",i,"Marks :",(sum/5))
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
    print("Congratulations !! ",max_i,"...You are the Topper of Class...")
    

marks(nisha=[98,99,97,95,70],rutika=[94,98,99,96,95],shraddha=[99,95,97,90,93],pranita=[20,96,94,95,90],tanuja=[30,91,99,98,97],kane=[99,98,99,97,99])'''

#anonymous function (lambda function)

'''add = lambda a,b:a+b
print(add(20,30))'''

'''add = lambda a=20,b=40:a+b
print(add())'''

'''add = lambda a,b:a+b
sub = lambda a,b:a-b
mul = lambda a,b:a*b
div = lambda a,b:a/b
pwr = lambda a,b:a**b
sqr = lambda a:a*a
sqt = lambda a:a**0.5
print(add(20,30))
print(sub(50,30))
print(mul(20,3))
print(div(20,2))
print(pwr(20,2))
print(sqr(2))
print(sqt(4))'''

#lambda function with control statements
'''marks=lambda m,n: " greater m" if(m>n) else " greater n"
print(marks(90,50))'''

'''vote=lambda age:"eligible" if(age>=18) else "not eligible"
print(vote(19))'''

'''oddeven=lambda no:"even" if(no%2==0) else "odd"
print(oddeven(int(input("Enter : "))))'''

'''marks=lambda m,n: " greater m" if(m>n) else " greater n"
m=int(input("Enter 1: "))
n=int(input("Enter 2: "))
print(marks(m,n))'''


'''marks=lambda m,n:" greater m" if(m>n) else " greater n"
print(marks(int(input("Enter 1: ")),int(input("Enter 2: "))))'''

#greater 3 no.
'''m_no=lambda a,b,c:a if(a>b and a>c) else b if(b>c and b>a) else c
print(m_no(1,2,3))'''


#printing grade
grade=lambda m: "pass" if(m>40 and m<=50) else "2nd class" if (m>50 and m<=60) else "1st class" if(m>60 and m<=75) else "Distinction" if(m>75 and m<=100) else "Fail"
print(grade(int(input("Enter Per.: "))))
    





















