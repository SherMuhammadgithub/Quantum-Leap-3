import time

time_list = []
numbers_list = []

for i in range(1, 101):
    start_time = time.time()
    numbers_list.append(i)
    end_time = time.time()
    total_time  = end_time - start_time
    time_list.append(total_time)
    
    
    print(f"Appended {i} in {total_time:.10f} seconds")

    
