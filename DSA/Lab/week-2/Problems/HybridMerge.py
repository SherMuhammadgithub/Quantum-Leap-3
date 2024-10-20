from InsertionSort import InsertionSort
from MergeSrot import MergeSort
from funcs import measure_runtime, RandomArray

def HybridMergeSort(array, start, end):
    n = len(array)
    if n < 10:
        return InsertionSort(array, start, end)
    else:
        MergeSort(array, start, end)
    return array



def main():
    n_values = 30;
    random_array = RandomArray(n_values)
    HybridMergeSort_sort_time = measure_runtime(HybridMergeSort, random_array, 0, n_values - 1)
   
    with open('SortedHybridSort.csv', 'w') as file:
        for i in random_array:
            file.write(f"{i}\n")
    print(f"HybridMergeSort Sort Time: {HybridMergeSort_sort_time:.2f} ms")



if __name__ == '__main__':
    main()