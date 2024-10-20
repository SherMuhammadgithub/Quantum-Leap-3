import csv
import time
import random
from InsertionSort import InsertionSort
from MergeSrot import MergeSort

def read_words(filename):
    """Read words from a file and return a list of strings."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def write_csv(filename, data):
    """Write data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['N', 'InsertionSort Time (ms)', 'MergeSort Time (ms)', 'Shuffled InsertionSort Time (ms)', 'Shuffled MergeSort Time (ms)'])
        for row in data:
            writer.writerow(row)

def measure_runtime(func, data, start, end):
    """Measure the runtime of a function with given data and range in milliseconds."""
    import time
    data_copy = data[start:end + 1]
    start_time = time.time()
    func(data_copy, start, end)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert seconds to milliseconds

def ShuffleArray(array, start, end):
    """Shuffle the specified range of the array."""
    subarray = array[start:end + 1]
    random.shuffle(subarray)
    array[start:end + 1] = subarray

def main():
    # Read words from file
    words = read_words('words.txt')
    
    results = []
    
    # Define subset sizes
    subset_sizes = [100, 500, 1000]  # Adjust these values as needed
    
    for n in subset_sizes:
        if n > len(words):
            print(f"Warning: N={n} is greater than the number of words available.")
            continue
        
        # Extract subset of words if necessary
        words_subset = words[:n]
        
        # Measure runtime for InsertionSort
        insertion_sort_time = measure_runtime(InsertionSort, words_subset, 0, len(words_subset) - 1)
        
        # Measure runtime for MergeSort
        merge_sort_time = measure_runtime(MergeSort, words_subset, 0, len(words_subset) - 1)
        
        # Shuffle the words
        ShuffleArray(words_subset, 0, len(words_subset) - 1)
        
        # Measure runtime for InsertionSort on shuffled data
        shuffled_insertion_sort_time = measure_runtime(InsertionSort, words_subset, 0, len(words_subset) - 1)
        
        # Measure runtime for MergeSort on shuffled data
        shuffled_merge_sort_time = measure_runtime(MergeSort, words_subset, 0, len(words_subset) - 1)
        
        # Append results
        results.append([n, f"{insertion_sort_time:.2f}", f"{merge_sort_time:.2f}", f"{shuffled_insertion_sort_time:.2f}", f"{shuffled_merge_sort_time:.2f}"])
    
    # Write results to CSV
    write_csv('RunTime.csv', results)

if __name__ == '__main__':
    main()
