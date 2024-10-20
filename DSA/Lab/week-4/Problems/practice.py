def gnome_sort(arr):
    element_range = len(arr)
    index = 0

    while index < element_range:
        if index == 0:
            index += 1
        if arr[index] > arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1


def bingo_sort(input_array):
    
    bingo = min(input_array)
    next_bingo = max(input_array)

    next_position = 0
    while bingo < next_bingo:

        start_position = next_position
        for i in range(start_position, len(input_array)):
            if input_array[i] == bingo:
                input_array[i], input_array[next_position] = input_array[next_position], input_array[i]
                next_position += 1
            elif input_array[i] < next_bingo:
                next_bingo = input_array[i]

        bingo = next_bingo
        next_bingo = max(input_array)





def merge_sort(input_array):
    if len(input_array) <= 1:
        return input_array
    
    mid = len(input_array) // 2
    left_half = input_array[:mid]
    right_half = input_array[mid:]
    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        sorted_array.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        sorted_array.append(right[right_index])
        right_index += 1
    
    return sorted_array



def bubble_sort(input_array):
    for i in range(len(input_array) - 1):
        for j in range(0, len(input_array) - i - 1):
            if input_array[j] > input_array[j + 1]:
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
    


def selection_sort(input_array):
    for i in range(len(input_array) - 1):
        min_index = i
        for j in range(i + 1, len(input_array)):
            if input_array[j] < input_array[min_index]:
                min_index = j
        if min_index != i:
            input_array[i], input_array[min_index] = input_array[min_index], input_array[i]


def quick_sort(input_array, low, high):
    if low < high:
        pivot_index = partition(input_array, low, high)

        quick_sort(input_array, low, pivot_index - 1)
        quick_sort(input_array, pivot_index + 1, high)


def partition(input_array, low, high):
    pivot = input_array[high]
    i = low - 1
    for j in range(low, high):
        if input_array[j] < pivot:
            i += 1
            input_array[i], input_array[j] = input_array[j], input_array[i]
    input_array[i + 1], input_array[high] = input_array[high], input_array[i + 1]
    return i + 1

input_array = [54,31,59,67,65]
quick_sort(input_array, 0, len(input_array) - 1)
print(input_array)

