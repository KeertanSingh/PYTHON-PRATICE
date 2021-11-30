
def calcutor():

   n1 = int(input("Enter first number here:"))
   n2 = int(input("Enter second number here:"))
   operation = input("What do you wanna do?\n Press 1 for addition\n Press 2 for subtraction\n Press 3 for "
                     "multiplication\n Press 4 for divison\n>>>")

   if operation=="1":
       print("Sum of",n1,"and",n2,"=",n1 +n2)

   elif operation == "2":
       print("Difference between",n1,"and",n2,"=",n1-n2)

   elif operation =="3":
       print("product of both numbers =",n1*n2)

   elif operation == "4":
       print("Division=",n1/n2)
   else:
       print("Something is wrong")
   again()

def again():
    ask = input("Do you wanna run it again?\n")
    if ask == "yes":
        calcutor()
    else:
        print("Thanks you")

calcutor()