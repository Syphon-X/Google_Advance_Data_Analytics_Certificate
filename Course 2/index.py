

# Getting Started with Python #

#-----------Module 1-----------#
print('-----------Module 1-----------')

# print('Hello World!')

# x = 1
# y = 2
# sum = x + y
# print(sum)

# Example of Classes and how they can be used.

class Spaceship:
    # Class attribute
    tractor_beam = 'off'
    
    # Instance attributes
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.speed = None

    # Instance methods
    def warp(self, warp):
        self.speed = warp
        print(f'Warp {warp}, engage!')

    def tractor(self):
        if self.tractor_beam == 'off':
            self.tractor_beam = 'on'
            print('Tractor beam on.')
        else:
            self.tractor_beam = 'off'
            print('Tractor beam off.')


ship = Spaceship('Mockingbird', 'Rescue Frigate')

print(ship.name)
print(ship.kind)
print(f'Tractor beam is: {ship.tractor_beam}')

ship.warp(7)
print(ship.speed)


ship.tractor()
print(ship.tractor_beam)


class ID:
    #class attribute
    
    #instance attributes
    def __init__(self, name, gender, age, student=True):
        self.name = name
        self.gender = gender
        self.age = age
        self.student = student
        
    #instance methods
    def is_student(self):
        if self.student == True:
            print(f'{self.name} is a student.')
        else:
            print(f'{self.name} is not a student.')


id1 = ID('Ted', 'Male', '35', True)

print(id1.name)
id1.is_student()


#-----------Module 2-----------#
print('-----------Module 2-----------')

# Function, Clean Code, Commenting, Operators( >, <, and, or), Conditional Statements 

# refactoring is the process of restructuring code while maintaining its original functionality

# self-documentating code is when code is written in a way that is readible and makes its purpose clear


def testfunc(name):
    '''This is an example of a docstring.  This is to help with providing notes on what something does.'''
    print(f'Hi there {name}!')

testfunc('Ted')



#-----------Module 3-----------#

# Loops, while.


#-----------Module 4-----------#
print('-----------Module 4-----------')

fruit_list = ['strawberry', 'banana', 'pineapple', 'apple']

fruit_list.append('kiwi')
print(fruit_list)

fruit_list.insert(0, 'orange')
print(fruit_list)

fruit_list.remove('banana')
print(fruit_list)

fruit_list[1] = 'mango'
print(fruit_list)

# zip() , can zip up more than two sequences.

cities = ['Paris', 'Lagos', 'Mumbai']
countries = ['France', 'Nigeria', 'India']
places = zip(cities, countries)


print(places)
print(list(places))

# unzipping by adding *
scientists = [('Nikola', 'Tesla'), ('Charles', 'Darwin'), ('Marie', 'Curie')]
given_names, surnames = zip(*scientists)
print(given_names)
print(surnames)

#enumerate is similar to zip, but also adds the index number as well
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print(index, letter)

# dictionaries: has a key value pair and are mutable
zoo = {
    'pen1': 'penguin',
    'pen2': 'zebras',
    'pen3': 'lions',
}

zoo['pen4'] = 'crocodile'
print(zoo['pen4'])


# Arrays and vectors with NumPy
# Libraries or Packages are a collection of reusable code









