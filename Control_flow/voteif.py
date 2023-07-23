age=int(input("Enter age : "))
if(age>=18):
    print("Eligible")
    vid=input("Do you have voter id ?? ")
    if(vid=='yes'):
        print("Ok..you are eligible...")
    else:
         print("No..you are not eligible...")
else :
    print("Not eligible")
