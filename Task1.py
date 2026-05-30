def is_increasing(num):
    is_increasing_number = True

    num = str(num)
    
    for i in range(len(num)):
        if i != 0:
            current_digit = int(num[i])
            previous_digit = int(num[i-1])
            if previous_digit > current_digit:
                is_increasing_number = False

    return is_increasing_number

def is_decreasing(num):
    is_decreasing_number = True

    num = str(num)
    
    for i in range(len(num)):
        if i != 0:
            current_digit = int(num[i])
            previous_digit = int(num[i-1])
            if previous_digit < current_digit:
                is_decreasing_number = False

    return is_decreasing_number

def is_bouncy(num):
    if (not is_increasing(num)) and (not is_decreasing(num)):
        return True
    return False

def is_perfectly_bouncy(num):
    if not is_bouncy(num):
        return False
    
    num = str(num)

    number_followed_by_larger = 0
    number_followed_by_smaller = 0

    for i in range(len(num)):
        if i != 0:
            current_digit = int(num[i])
            previous_digit = int(num[i-1])
            if previous_digit < current_digit:
                number_followed_by_larger += 1
            elif previous_digit > current_digit:
                number_followed_by_smaller += 1

    return number_followed_by_larger == number_followed_by_smaller


valid = False
while not valid:
    number = int(input("Enter a number: "))
    if number > 0:
        valid = True

if is_perfectly_bouncy(number):
    print("This number is perfectly bouncy")
elif is_bouncy(number):
    print("This number is bouncy")
else:
    print("This number is not bouncy")