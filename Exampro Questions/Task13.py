print("Enter a positive whole number: ")
NumberIn = int(input())

NumberOut = 0 

Count = 0
while NumberIn > 0:
    Count = Count + 1

    PartValue = NumberIn % 2
    NumberIn = NumberIn // 2

    for i in range(1, Count):
        PartValue = PartValue * 10

    NumberOut = NumberOut + PartValue

print("The result is: " + str(NumberOut))