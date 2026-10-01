limit = int (input("enter your number:"))
for i in range (1,1+limit):
    if i % 2 == 0 :
        print(i, "-Even")
    else:
        print(i, "-Odd")
age = int(input("enter your age:"))
if age >= 18 :
    print("elibible for voting")
else:
    print("unelibile for voting ")