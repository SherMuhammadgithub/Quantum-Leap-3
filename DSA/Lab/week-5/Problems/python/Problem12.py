integer_list  = [] 

def remove_negative_integers():
    for i in range(len(integer_list)):
        if integer_list[i] < 0:
            integer_list.remove(integer_list[i])
                       
def find_max_min():
    min_value = integer_list[0]
    max_value = integer_list[len(integer_list) - 1]
    
    for i in range(1, len(integer_list)):
        if integer_list[i] < min_value:
            min_value = integer_list[i]
            
    for j in range(len(integer_list) - 1):
        if integer_list[j] > max_value:
            max_value = integer_list[i]
            
    return min_value + "," + max_value

def compute_avg():
    sum_value = 0
    for i in range(len(integer_list)):
        sum_value += integer_list[i]
        
    average = sum_value // len(integer_list)
    return average

        