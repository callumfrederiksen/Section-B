def calculate_top_frequency(input_values):
    frequency_dictionary = {}
    for n in input_values:
        if n in frequency_dictionary:
            frequency_dictionary[n] += 1
        else:
            frequency_dictionary[n] = 1

    top_frequency = 0
    for n in list(frequency_dictionary.keys()):
        if frequency_dictionary[n] > top_frequency:
            top_frequency = frequency_dictionary[n]

    numbers_with_top_frequency = 0
    for n in list(frequency_dictionary.keys()):
        if frequency_dictionary[n] == top_frequency:
            numbers_with_top_frequency += 1

    if numbers_with_top_frequency == 1:
        return f'The top frequency of the input values is: {top_frequency}'
    else:
        return "Data was multimodal"

num_of_inputs = int(input("Enter the number of elements that you would like to input: "))
input_values = []
for i in range(num_of_inputs):
    input_values.append(int(input("Enter value " + str(i + 1) + ": ")))

print(calculate_top_frequency(input_values))