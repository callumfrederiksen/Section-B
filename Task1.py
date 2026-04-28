import math

string_entered = input()
columns_entered = int(input())

def validate(string):
    returned_string = ""
    for l in string:
        if (ord(l) >= 97 and ord(l) <= 97+25) or (ord(l) >= 65 and ord(l) <= 90):
            returned_string += l
    return returned_string

def railfence(string, columns):
    string = validate(string)
    toreturn = ""
    rows = math.ceil(len(string) / columns)
    for i in range(columns):
        j = 0
        while j+i < len(string):
            toreturn += string[j + i]
            j += columns
    return toreturn

print(railfence(string_entered, columns_entered))
