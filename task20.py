num1=float(input("enter the first value:"))
op=input("enter operator(+,-,*,%):")
num2=float(input("enter the second value:"))
if op == '+':
    print(f"the result is:{num1 + num2}")
elif op =='-':
      print(f"the result is:{num1 - num2}")
elif op =='*':
      print(f"the result is:{num1 * num2}")
elif op == '/':
     if num2 != 0:
          print(f"the result is:{num1 / num2}") 
     else :
           print("Error:Divission by zero is not allowed ")
else : 
     print("invalied operator")
