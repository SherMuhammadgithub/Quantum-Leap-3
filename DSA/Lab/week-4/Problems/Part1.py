def partition(input_array, low, high):
    pivot = input_array[high]

    i = low - 1
    for j in range(low, high):
        if input_array[j] < pivot:
            i += 1
            input_array[i], input_array[j] =input_array[j], input_array[i]

    input_array[i + 1], input_array[high] = input_array[high], input_array[i + 1]
    return i + 1

def quick_sort(input_array, low, high):
    if low < high:
        pivot = partition(input_array, low, high)

        quick_sort(input_array, low, pivot - 1)
        quick_sort(input_array, pivot + 1, high)


input_array = [12,90,23,56,234,0,234,5,2,6]

quick_sort(input_array, 0, len(input_array) - 1)

print(input_array)