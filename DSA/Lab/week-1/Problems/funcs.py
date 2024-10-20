# prolem-1
def SearchA(arr,x):
    newArray = []
    for i in range(len(arr)):
        if arr[i] == x:
            newArray.append(i)
    return newArray

# driver
# print(SearchA([22,2,1,7,11,13,5,2,9] , 2))

# problem-2
def SearchB(Arr, x):
    newArray = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            newArray.append(i)
            if(Arr[i] > x):
                break
    
    return newArray

# driver
# print(SearchB([22,2,1,7,11,13,5,2,9] , 2))

# problem-3
def Minimum(Arr, startingIndex, endingIndex):
    minIndex  = startingIndex
    for i in range(startingIndex + 1, endingIndex + 1):
        if Arr[i] < Arr[minIndex]:
            minIndex = i
    return minIndex

 # driver   
# print(Minimum([3,4,7,8,0,1,23,-2,-5], 7, 5))

# problem-4
def Sort4(Arr):
    for i in range(len(Arr)):
        minIndex = Minimum(Arr, i, len(Arr)-1)
        Arr[i], Arr[minIndex] = Arr[minIndex], Arr[i]
    return Arr

# driver
# print(Sort4([-5, -4, -3, 0, 1, 1, 4, 35, 100, 101]))

# probelm-5
def StringReverse(str, staringIndex, endingIndex):
    reversedStringArray = []
    for i in range(endingIndex, staringIndex - 1, -1):
        print(str[i])
        reversedStringArray.append(str[i])
    #converting the array in
    reversedString = ""
    return reversedString.join(reversedStringArray)

# driver
# print(StringReverse("University of Engineering and Technology Lahore", 1 , 10))

# problem-6
def SumIterative(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum
    
# driver
# print(SumIterative(1524))

# via recursion
def SumRecursive(number):
    while number > 0:
        return number % 10 + SumRecursive(number // 10)
    return 0

# driver
# print(SumRecursive(1524))

# problem-7
def ColumnWiseSum(Mat):
    newarr = []
    for i in range(len(Mat)):
        sum = 0
        for j in range(len(Mat[i])):
            sum += Mat[j][i]
        newarr.append(sum)
    return newarr
# driver
# print(ColumnWiseSum([[1, 13, 13], [5,11, 6], [4, 4, 9]]))


def RowWiseSum(Mat):
    newArr = []
    for i in range(len(Mat)):
        sum = 0
        for j in range(len(Mat[i])):
            sum += Mat[i][j]
        newArr.append(sum)
    return newArr

# driver
# print(RowWiseSum([[1, 13, 13], [5,11, 6], [4, 4, 9]])) 

# problem 8
def SortedMerge(Arr1, Arr2):
    i = 0
    j = 0
    newArr = []
    while i < len(Arr1) and j < len(Arr2):
        if Arr1[i] < Arr2[j]:
            newArr.append(Arr1[i])
            i += 1
        else:
            newArr.append(Arr2[j])
            j += 1
    while i < len(Arr1):
        newArr.append(Arr1[i])  
        i += 1
    while j < len(Arr2):
        newArr.append(Arr2[j])
        j += 1
    return newArr

# driver
# print(SortedMerge( [0,3,4,10,11], [1,8,13,24]))

# problme-9
def PalindromRecursive(str):
    if len(str) <= 1:
        return True
    else:
        return str[0] == str[-1] and PalindromRecursive(str[1:-1])

# driver
# print(PalindromRecursive("radar"))

# problem-10 
def Sort10(Arr):
    sorted_array = Sort4(Arr)
    print(sorted_array)
    non_negative_nums = []
    negative_nums = []

    for i in range(len(sorted_array)):
        if sorted_array[i] > 0:
            non_negative_nums.append(sorted_array[i])
        else:
            negative_nums.append(sorted_array[i])

    resultant_array = []
    i = 0
    j = 0

    while i < len(negative_nums) or j < len(non_negative_nums):
        if i < len(negative_nums):
            resultant_array.append(negative_nums[i])
            i += 1
        if j < len(non_negative_nums):
            resultant_array.append(non_negative_nums[j])
            j += 1

    return resultant_array

# driver
# print(Sort10([10, -1, 9, 20, -3, -8, 22, 9, 7]))