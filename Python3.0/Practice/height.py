height_in_cm = int(input("Enter you height in cm : "))
cm_to_inches = 1 / 2.54
cm_to_foot = 1/(12*2.54)
print(f"Height in foot : {cm_to_foot* height_in_cm}")
print(f"Height in inch: {cm_to_inches*height_in_cm}")
