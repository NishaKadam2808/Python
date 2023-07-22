'''****
   ****
   ****
   **** 
for j in range(4):
    for i in range(4):
        print("*",end=' ')
    print()'''

'''
* 
* * 
* * * 
* * * *
for j in range(4):
    for i in range(j+1):
        print("*",end=" ")
    print()'''

'''
* * * * 
* * * 
* * 
* 
for j in range(4):
    for i in range(4-j):
        print("*",end=" ")
    print()'''


'''
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
for j in range(4):
    for i in range(j+1):
        print("*",end=" ")
    print()
for j in range(3):
    for i in range(3-j):
        print("*",end=" ")
    print()


