a=eval(input("Enter an initial list : "))
b=eval(input("Enter the finial list : "))
print("*****INITIAL PUZZLE*****")
for i in range(len(a)):
    print(a[i])
print("*****FINAL PUZZLE*****")
for i in range(len(b)):
    print(b[i])
z=1
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]==b[i]:
            continue
        else:
            a[i]=b[i]
            print("STEP : ",z)
            for i in range(len(a)):
                print(a[i])
            z+=1


