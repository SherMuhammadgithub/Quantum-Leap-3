
import csv
import random

def read_values(filename):
    """Read values from a file and return a list of integers."""
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def write_csv(filename, data):
    """Write data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['N', 'InsertionSort Time', 'SelectionSort Time'])
        for row in data:
            writer.writerow(row)

def measure_runtime(func, data, start, end):
    """Measure the runtime of a function with given data and range in milliseconds."""
    import time
    start_time = time.time()
    func(data, start, end)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert seconds to milliseconds

def RandomArray(size):
    newArray = []
    for i in range(size):
        randomNumber = random.randint(0, 30000)
        newArray.append(randomNumber)
    return newArray