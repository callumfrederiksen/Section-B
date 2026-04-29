number  = int(input("Enter Number: "))

def isInt(number):
    return int(number) == number

def isPrime(number):
    for i in range(2, number):
        dividend = number / i
        if isInt(dividend):
            return False
    return True

def primeDecomp(number):
    prime_factors = []
    i = 2
    while not isPrime(number):
        dividend = number / i
        if isInt(dividend):
            number = int(dividend)
            prime_factors.append(i)
            i = 2
        i += 1
    prime_factors.append(int(number))
    return prime_factors

def intSum(number):
    total = 0
    number = str(number)
    for l in number:
        total += int(l)
    return total 

def isSmithNumber(number):
    primeFactorDigitTotal = 0
    numberDigitTotal = intSum(number)
    primeFactors = primeDecomp(number)
    for factor in primeFactors:
        primeFactorDigitTotal += intSum(factor)
    return numberDigitTotal == primeFactorDigitTotal 

if isSmithNumber(number):
    print("Smith Number")
else:
    print("Not a Smith Number")