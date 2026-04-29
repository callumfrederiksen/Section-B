number = int(input("Enter a number: "))

def happy_number(number, list=[]):
    if number in list:
        return False

    new_list = list + [number]

    str_number = str(number)
    new_number = 0
    for l in str_number:
        new_number += int(l) ** 2

    print(new_number)
    if new_number == 1:
        return True

    return happy_number(new_number, list=new_list)
    
is_happy_number = happy_number(number)

if is_happy_number:
    print("Happy Number")
else:
    print("Not Happy Number")
    