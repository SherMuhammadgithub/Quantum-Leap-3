from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from funcs import read_values, write_csv, measure_runtime, RandomArray




def main():
    # Read values from file
    n_values = read_values('Nvalues.txt')
    
    results = []
    
    for n in n_values:
        # Generate a list of random integers or use a fixed list for testing
        test_data = RandomArray(n)
        
        # Measure runtime for InsertionSort
        insertion_sort_time = measure_runtime(InsertionSort, test_data.copy(), 0, n - 1)
        
        # Measure runtime for SelectionSort
        selection_sort_time = measure_runtime(SelectionSort, test_data.copy(), 0 , n - 1)
        
        # Append results
        results.append([n, f"{insertion_sort_time:.2f}", f"{selection_sort_time:.2f}"])
    
    # Write results to CSV
    write_csv('RunTime.csv', results)

if __name__ == '__main__':
    main()
