# Exponent function

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num

    return result

if __name__ == '__main__':
    base_num = int(input("Enter the base number: "))
    power_num = int(input("Enter the power number: "))
    power = raise_to_power(base_num, power_num)
    print(power)
