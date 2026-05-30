def RLE_encode(string):
    rle_string = ""

    current_char = ""
    current_char_count = 0

    for c in string:
        if c == current_char:
            current_char_count += 1
        else:
            if current_char_count > 0:
                rle_string += current_char + " " + str(current_char_count) + " "
            current_char = c
            current_char_count = 1

    rle_string += current_char + " " + str(current_char_count)

    return rle_string

string = input("Enter string to be encoded: ")
print(RLE_encode(string))