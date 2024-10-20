import random
import csv
from funcs import measure_runtime, RandomArray




def InsertionSort(array, start, end):
    for j in range(start + 1, end + 1):
        i = j - 1
        key = array[j]
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array
        
            
def main():
    n_values = 30;
    random_array = RandomArray(n_values)
    insertion_sort_time = measure_runtime(InsertionSort, random_array, 0, n_values - 1)

    with open('SortedInsertionSort.csv', 'w') as file:
        for i in random_array:
            file.write(f"{i}\n")
    print(f"Insertion Sort Time: {insertion_sort_time:.2f} ms")



if __name__ == '__main__':
    main()