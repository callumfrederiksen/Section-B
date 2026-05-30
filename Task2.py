def string_is_valid(string_entered):
    valid = True
    if not (len(string_entered) >= 5 and len(string_entered) <= 7):
        valid = False

    for l in string_entered:
        if not (ord(l) >= 65 and ord(l) <= 90):
            valid = False

    letters_appeared = []
    for l in string_entered:
        if l in letters_appeared:
            valid = False
        letters_appeared.append(l)

    ascii_sum = 0
    for l in string_entered:
        ascii_sum += ord(l)
    if not (ascii_sum >= 420 and ascii_sum <= 600):
        valid = False

    return valid

is_valid = False
while not is_valid:
    string_entered = input("Enter a string to be validated: ")
    if string_is_valid(string_entered):
        print("String is valid")
        is_valid = True
    else:
        print("String is not valid")