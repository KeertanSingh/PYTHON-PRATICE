
principal = float(input("Enter the principal : "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time period : "))

# rate = rate/100
simple_interest = (principal*rate*time)/100 #A = p(1+rt)
compount_interest = (principal * (1 + rate/100)**time) -principal
print(f"Principal={principal}       Rate={rate} year     Time={time}")
print(f"Simple interest = {simple_interest}")
print(f"Compound interest = {compount_interest}")

