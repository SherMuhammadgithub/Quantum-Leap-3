def count_sort(input_array):
    max_value = max(input_array)
    min_value = min(input_array)

    range_of_elements = max_value - min_value + 1
    count_array = [0] * range_of_elements

    for num in input_array:
        count_array[num - min_value] += 1

    for i in range(1,range_of_elements):
        count_array[i] += count_array[i -1]

    output_array = [0] * len(input_array)
    for i in range(len(input_array) - 1, -1 , -1):
        output_array[count_array[input_array[i] - min_value] - 1] = input_array[i]
        count_array[input_array[i] - min_value] -= 1

    return output_array



# print(count_sort([-5, -10, 0, -3, 8, 5, -1, 10]))

# buckets = [[] for _ in range(10)]
# print(buckets)

def insertion_sort(input_array):
    for i in range(1,len(input_array)):
        key = input_array[i]
        j = i - 1

        while j >= 0 and key < input_array[j]:
            input_array[j + 1] = input_array[j]
            j -= 1

        input_array[j + 1] = key



def bucket_sort(input_array):
    element_range = len(input_array)
    # temp array for buckets
    buckets = [[] for _ in range(element_range)]

    # insert elements in bucket
    for num in input_array:
        bi = int(num * element_range)
        buckets[bi].append(num)
     # sort each bucket
    for bucket in buckets:
        insertion_sort(bucket) 

    
    # concatenate sort buckets in signle array
    index = 0
    for bucket in buckets:
        for num in bucket:
            input_array[index] = num
            index += 1

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(arr)
print("Sorted array is:")
print(" ".join(map(str, arr)))
