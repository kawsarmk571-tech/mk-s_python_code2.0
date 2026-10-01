n=int(input("entre the value:"))
even_sum = 0
odd_sum = 0
for i in range (1,n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i 
print(f"the even number is:{even_sum}")
print(f"the odd number is:{odd_sum}")
