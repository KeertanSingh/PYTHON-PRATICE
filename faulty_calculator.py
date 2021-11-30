#45*3=555 56+9=77 56/6=4
operation = input("FAULTY CALCULATOR\nPress 1 for addition\nPress 2 for substraction\nPress 3 for multiplication\nPress 4 for division\n>>")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

#faluty condition


if operation =="1" and num1==56 and num2==9 :
    print("77")
elif operation=="1" and num1==9 and num2==56:
    print("77")

elif operation=="3" and num1==45 and num2==3 :
    print("555")
elif operation=="3" and num1==3 and num2==45:
    print("555")

elif operation=="4" and num1 ==56 and num2==6  :
    print("4")
elif operation=="4" and num1 ==6 and num2==56:
    print("4")



#addition
elif operation =="1" :
    print("Sum of both number =",num1+num2)



#substraction
elif operation=="2" :
    print("Difference between both number=",num1-num2)




#multiplication
elif  operation=="3":
    print("Product between both number=",num1*num2)



#division
elif operation=="4":
    print("Division between both number=",num1/num2)



else:
    print("Something is wrong!!")








