def is_harshad(num):
    digits = [int(d) for d in str(num)]

    digit_sum = 0
    for d in digits:
        digit_sum += d

    return num % digit_sum == 0

def nth_harshad_number(n):
    numbers_found = 0
    i = 0
    while numbers_found < n:
        i += 1
        if is_harshad(i):
            numbers_found += 1
    return i

number = int(input("Enter to find nth harshad number: "))
print(nth_harshad_number(number))
