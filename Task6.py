def is_prime(num):
    prime_number = True
    for i in range(2, num):
        if num % i == 0:
            prime_number = False

    return prime_number

running = True
while running:
    number = int(input("Enter a number: "))
    if not number > 1:
        print("Number not greater than 1")
    elif is_prime(number):
        print("Number is prime")
    else:
        print("Number is not prime")

    run_again = input("Run again? (Y/N/y/n): ")
    if run_again in ['N', 'n']:
        running = False