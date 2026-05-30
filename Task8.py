def convert_number_to_binary(number, binary_string=""):
    if number == 0:
        return binary_string
    
    dividend = number // 2
    remainder = number % 2

    binary_string = str(remainder) + binary_string
    return convert_number_to_binary(dividend, binary_string=binary_string)

number = int(input("Enter a number to convert to binary: "))
print(convert_number_to_binary(number))