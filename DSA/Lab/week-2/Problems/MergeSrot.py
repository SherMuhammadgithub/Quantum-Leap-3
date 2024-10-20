from funcs import measure_runtime, RandomArray

def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
    return array


def Merge(Arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = [0] * (n1 + 1) 
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = Arr[start + i]
    for j in range(n2):
        R[j] = Arr[mid + j + 1]
    L[n1] = 300000
    R[n2] = 300000
    i = 0
    j = 0
    for k in range(start, end + 1):
        if L[i] <= R[j]:    
            Arr[k] = L[i]
            i = i + 1
        else:
            Arr[k] = R[j]
            j = j + 1
    return Arr


def main():
    n_values = 30000;
    random_array = ["e","f","a,""b","c","d"]
    merge_sort_time = measure_runtime(MergeSort, random_array, 0, n_values - 1)
   
    with open('SortedMergeSort.csv', 'w') as file:
        for i in random_array:
            file.write(f"{i}\n")
    print(f"MergeSort Sort Time: {merge_sort_time:.2f} ms")



if __name__ == '__main__':
    main()