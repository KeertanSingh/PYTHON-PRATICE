import math


def surface_area(radius):
    print(f"Surface area of sphere = {4 * math.pi * radius ** 2}")


def volume(radius):
    print(f"Volume of sphere = {(4 / 3) * math.pi * radius ** 3}")


if __name__ == '__main__':
    r = int(input("Enter the radius of sphere: "))
    choice = int(input("""1. Area of sphere
2. Volume of sphere
>> """))
    if choice == 1:
        surface_area(r)
    elif choice == 2:
        volume(r)
    else:
        print("Invalid input!!")
