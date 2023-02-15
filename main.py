""" Arrays"""

my_students = ['Katrina', 'Anna', 'Victoria', 'Annemieke', 'Pola']  # list

print(type(my_students))

# deletion

my_students.pop()
print(my_students)
my_students.remove('Anna')
print(my_students)

# also:
last_student = my_students.pop()
print(last_student)

# also built in sort function
my_students = ['Katrina', 'Anna', 'Victoria', 'Annemieke', 'Pola']  # list
print('My students before sorting', my_students)
my_students.sort()
print('My students after sorting', my_students)

