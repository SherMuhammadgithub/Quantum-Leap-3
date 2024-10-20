from funcs import measure_runtime, RandomArray

def SelectionSort(array, start, end):
    for i in range(start, end):
        minIndex = i
        for j in range(i + 1, end + 1):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array





def main():
    n_values = 30;
    random_array = RandomArray(n_values)
    SelectionSort_sort_time = measure_runtime(SelectionSort, random_array, 0, n_values - 1)
   
    with open('SortedSelectionSort.csv', 'w') as file:
        for i in random_array:
            file.write(f"{i}\n")
    print(f"SelectionSort Sort Time: {SelectionSort_sort_time:.2f} ms")



if __name__ == '__main__':
    main()
