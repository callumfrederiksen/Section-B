print("Enter a number greater than 1: ")
Number = int(input())

X = 2

Count = 0
while Number > 1:
    Multi = False
    while Number % X == 0:
        if not Multi:
            print(X)
        
        Count = Count + 1
        Multi = True
        Number = Number // X
    X = X + 1

print(Count)