Number = 0
while Number < 1 or Number > 10:
    print("Enter a positive whole number: ")
    Number = int(input())

    if Number > 10:
        print("Number too large")
    elif Number < 1:
        print("Not a positive number")
        
c = 1
for k in range(Number):
    print(c)
    c = (c * (Number - 1 - k)) // (k + 1)