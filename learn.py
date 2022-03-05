# lists and dictionaries comprehension in python
# new_list = [new_item for item in list]
numbers = [10, 20, 30]
new_numbers = [number + 1 for number in numbers]
print(new_numbers)

# list, range, strings and tuples etc in python are called sequences because they try to follow a specific order

new_range_numbers = [num * 2 for num in range(1, 5)]
print(new_range_numbers)

# conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# a new list of short names
short_names = [name for name in names if len(name) <= 5]
print(short_names)
long_names_upper = [name.upper() for name in names if len(name) >= 5]
print(long_names_upper)

def count_zeeros(list):
    zeros_arr = [number for number in list if number == 0]
    return len(zeros_arr)

print(count_zeeros([10, 0, 5, 3, 5, 0]))

# LIST COMPREHENSION EXERCISES
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]
print(squared_numbers)

# filtering even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)

# iterating over pandas dataframe
import pandas
student_dict = {
    "student":["Dennis", "Jack", "Lily"],
    "score": [98, 88, 80]
}
for (key, value) in student_dict.items():
    print(key,  value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# looping through the data frame
for (key, value) in student_data_frame.items():
    print(value)

for (index, row) in student_data_frame.iterrows():
    print(row.student)

# Dictionary comprehension
# {new_key:new_value for (key, value) in dict.items()}
# {new_key:new_value for (index, row) in dataframe.iterrows()}