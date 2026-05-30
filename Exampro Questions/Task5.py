def letter_decomposition(string):
    letter_frequency_dictionary = {}

    for l in string:
        if l in letter_frequency_dictionary:
            letter_frequency_dictionary[l] += 1
        else:
            letter_frequency_dictionary[l] = 1

    return letter_frequency_dictionary

def can_be_constructed(original_string, string_to_be_constructed):
    dictionary = letter_decomposition(original_string)

    can_be_constructed = True
    for l in string_to_be_constructed:
        if l not in dictionary:
            can_be_constructed = False
        else:
            if dictionary[l] <= 0:
                can_be_constructed = False
            dictionary[l] -= 1

    return can_be_constructed

string1 = input("Enter string to be constructed: ")
string2 = input("Enter string providing letters: ")
if can_be_constructed(string2, string1):
    print("The string can be constructed")
else:
    print("The string cannot be constructed")