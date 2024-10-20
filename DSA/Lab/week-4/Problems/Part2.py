def counting_sort(input_array, exp):
    element_range = len(input_array)
    output_array = [0] * element_range
    count_array = [0] * 10

    for i in range(0, element_range):
        index = input_array[i] // exp
        count_array[index % 10] += 1
    
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    i = element_range - 1
    while i >= 0:
        index = input_array[i] // exp
        output_array[count_array[index % 10] - 1] = input_array[i]
        count_array[index % 10] -= 1
        i -= 1
    
    for i in range(element_range):
        input_array[i] = output_array[i]


def radix_sort(input_array):
    max_value = max(input_array)
    
    exp = 1
    while max_value / exp >= 1:
        counting_sort(input_array, exp)
        exp *= 10


input_array = [110, 45, 65, 50, 90, 602, 24, 2, 66]
radix_sort(input_array)

print(input_array)