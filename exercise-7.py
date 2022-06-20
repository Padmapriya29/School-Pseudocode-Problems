num1 = int(input("Enter number one here: "))
num2 = int(input("Enter number two here: "))
num3 = int(input("Enter number three here: "))
if num1>num2 and num2>num3:
    print("The order is: ",num1, num2, num3)
elif num2>num1 and num1>num3:
    print("The order is: ",num2, num1, num3)
elif num3>num1 and num1>num2:
    print("The order is: ",num3, num1, num2)
elif num3>num2 and num2>num1:
    print("The order is: ",num3, num2, num1)
elif num2>num3 and num3>num1:
    print("The order is: ",num2, num3, num1)
elif num1>num3 and num3>num2:
    print("The order is: ",num1, num3, num2)
else:
    print("The numbers ar equal")
    
