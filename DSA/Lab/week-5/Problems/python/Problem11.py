students_list = ["sher", "ali", "khan"]

def search_student(std_name):
    for i in range(len(students_list)):
        if students_list[i] == std_name:
            return "index: "+ str(i) + " and name: "+ std_name
        
    return "Student not Found"

print(search_student("khan"))
            