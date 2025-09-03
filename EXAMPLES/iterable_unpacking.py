values = ['a', 'b', 'c']

x, y, z = values  # unpack values (which is an iterable) into individual variables

print(x, y, z)
print()

#  () [] {}

people = [
    ('Bill', 'Gates', 'Microsoft'), 
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux', 'git'),
    ('John', 'Strickler'),
]

for person_tuple in people:
    first_name, last_name, *_ = person_tuple  # unpack row into variables
    print(first_name, last_name, _)  # _ is list of leftovers
print()

for first_name, last_name, *_ in people:  # a for loop unpacks if there is more than one variable
    print(first_name, last_name)
print()

print(f"{people[0] = }")
print(f"{people[0][0] = }")
print(f"{people[0][0][0][0][0][0] = }")


