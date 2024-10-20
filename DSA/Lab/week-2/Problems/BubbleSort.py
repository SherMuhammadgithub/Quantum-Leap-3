from funcs import measure_runtime, RandomArray

def BubblSort(Arr, start, end):

    for i in range(end):
        for j in range(start, end - i):
            if Arr[j] > Arr[j + 1]:
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
    return Arr;



def main():
    n_values = 1000;
    random_array = RandomArray(n_values)
    BubblSort_sort_time = measure_runtime(BubblSort, random_array, 0, n_values - 1)
   
    with open('SortedBubbleSort.csv', 'w') as file:
        for i in random_array:
            file.write(f"{i}\n")
    print(f"BubblSort Sort Time: {BubblSort_sort_time:.2f} ms")



if __name__ == '__main__':
    main()