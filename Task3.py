def reverse_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_indices = []
    corresponding_vowels = []

    for i, l in enumerate(string):
        if l in vowels:
            vowel_indices.append(i)
            corresponding_vowels.append(l)

    for i in range(len(vowel_indices) // 2):
        n = len(corresponding_vowels) - 1
        corresponding_vowels[i], corresponding_vowels[n-i] = corresponding_vowels[n-i], corresponding_vowels[i]

    new_string = ""
    for i in range(len(string)):
        if i in vowel_indices:
            new_string += corresponding_vowels[vowel_indices.index(i)]
        else:
            new_string += string[i]

    return new_string

string = input("Enter a string: ")
print(reverse_vowels(string))