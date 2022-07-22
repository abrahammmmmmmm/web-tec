# list is an ordered sequence of items, most used datatypes[]
from unicodedata import name


list_of_numbers =[1,12,2,3,33,4,5]

list_of_numbers.extend([22,23,23,34,3])
print(list_of_numbers)

list_of_numbers[4] = 5
list_of_numbers[5] = 6

print(list_of_numbers.sort())
print(len(list_of_numbers))
print(list_of_numbers[0]) #-1 reverse the counting system
print(list_of_numbers[3:5])
print(list_of_numbers.sort(reverse=True))
list_of_numbers.append(26)
print(list_of_numbers)

print(type(list_of_numbers))
# tuple is an ordered sequence of iteams same as list
#the only d/ence is tuples are immutable
tuple_Of_numbers = (1,2,3,4,5,6)
  

#a set is unordered collection of unique items
a_set_of_numbers = {1,2,3,4,5,6,44,543}
print(a_set_of_numbers)

name = 'hanna'
print(name[1])

# a dictionary unordered collection of key value pairs
number_dict = {'name':'dave','age':21,'gender':'male'}
print(number_dict['name'])
