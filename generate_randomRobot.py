import pickle
import glob

class My_robots:

    known_colors = ['black', 'orange', 'blue', 'yellow', 'red', 'green']
    list_robots = []

    def __init__(self,name,number,color,function):
        import string
        import random
        if len(name) == 0:
            self.name = ''
            letters = string.ascii_letters
            numbers = string.digits
            for x in range(random.randint(3, 8)):
                self.name += random.choice(letters)
            self.name += '_'
            for x in range(random.randint(1, 3)):
                self.name += random.choice(numbers)
        else:
            self.name = name
        if number == 0:
            number = random.randint(1,100)
            self.number = number
        else:
            self.number = number
        if color in My_robots.known_colors:
            self.color = color
        else:
            self.color = 'unknown color'
        self.function = function
        My_robots.list_robots.append(self)

    def __str__(self):
        return f'Robot: {self.name}, Number: {self.number}, Color: {self.color}, Functions: {[x for x in self.function]}'

    def say_hi(self):
        print(f'My name is {self.name}. I have a number : {self.number} and i am {self.color}')
        if len(self.function) > 0:
            print('With functions: ')
            num = 1
            for func in self.function:
                print(f'{num}. {func}')
                num += 1
        print("*"*30)

    def save_to_file(self, path):
        with open(path, 'w+b') as f:
            pickle.dump(self,f)
            print('Save completed.')

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'r+b') as f:
            new_robot = pickle.load(f)
        cls.list_robots.append(new_robot)
        return new_robot

my_1_robot = My_robots('',0,'yellow',['clean','wash','cook'])
my_2_robot = My_robots('Easyn',0,'green',['eat','build'])
my_3_robot = My_robots('',0,'teal',[])

for r in My_robots.list_robots:
    r.save_to_file('my_robots.bin')

for i in My_robots.list_robots:
    print(i)

