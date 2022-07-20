# Almost everything in python is an object, strings, list, floats.

# When a variable is assigned to an onject. Variable is now an 'instance of that object'

# Objects have attributes that can be accessed via "." list.append() allows us to add to end of list. The '.append' is an attribute

# Related functions can be grouped into a class. A function inside a class is known as a method

spongebob = ['SpongeBob SquarePants', 'Fry Cook', 'Sea Sponge', 1500]
squidward = ['Squidward Tentacles', 'Cashier', 'Octopus', 700]
krabs = ['Eugene Krabs', 'Owner', 'Crab', 200000]
patrick = ['Patrick Star', 'Starfish', 0]

# Above code is better in a class. As it is difficult to remember what each index refers to in an instance of that object. 
# The object being the list and the name being the 'instance of that object'
 
def employee(name, position, species, salary):
    print({'Name' : name, 'Position': position, 'Species': species, 'Salary': salary})

spongebob = employee('SpongeBob SquarePants', 'Fry Cook', 'Sea Sponge', 1500)
squidward = employee('Squidward Tentacles', 'Cashier', 'Octopus', 700)
krabs = employee('Eugene Krabs', 'Owner', 'Crab', 200000)
patrick = employee('Patrick Star', None, 'Starfish', 0)

class ClassName:
    def __init__(self, param1, param2=1):
        self.param1 = param1
        self.param2 = param2

        self.param3 = param2 * 2

        self.param4 = 0

    def some_method(self, ext_input):
        return self.param1 + ext_input + ClassName.att

    def some_other_method(self, ext_input1, ext_input2):
        self.param4 = ext_input1 + ext_input2 # Changes the value of param4

class Employee:
    def __init__(self, name, position, species, total_hours, salary):
        self.name = name
        self.position = position
        self.species = species
        self.total_hours = total_hours
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount
        self.promotion()

    def work(self):
        self.total_hours += 1
        if self.total_hours % 40 == 0:
            self.increase_salary(50)

    def promotion(self):
        if self.salary > 200000:
            self.position = "Co-owner"

spongebob = Employee(name='SpongeBob SquarePants', position='Fry Cook', species='Sea Sponge', total_hours=0, salary=1500)

# If spongebob works 8 hours a day, 5 days a week, and 40 weeks a year
# what would his salary be at the end of the year?

for _ in range(8 * 5 * 40):
    spongebob.work()

print(spongebob.salary)

# How many hours does SpongeBob need to work to be promoted to co-owner?

while spongebob.position != "Co-owner":
    spongebob.work()

print(spongebob.total_hours)