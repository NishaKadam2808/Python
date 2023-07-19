#file handling
'''file handling is a process where we perform some operations on file usinf programming languages called File Handling'''

#write mode
'''data=open("demo_input.txt","w")
data.write("Computer")
data.close()'''

#append mode
'''data=open("demo_input.txt","a")
data.write("\n")
data.write("  Engineering")
data.close()'''

#table from 1 to 10
'''data=open("table.txt","w")
for i in range (1,11):
    for j in range (1,11):
        data.write(str(i*j))
        data.write("\t")
    data.write("\n")
data.close()'''

#read data
'''in_put=open("demo_input.txt","r")
out_put=in_put.read()
print(out_put)'''


