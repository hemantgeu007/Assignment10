'''Q1'''
class Animal():
    '''Animal Class Created'''
    def animal_attribute(self):
        '''animal_attribute() method defined'''
        print("This is Animal Class")

class Tiger(Animal):
    '''Tiger Class Created inheriting Animal Class'''
    def __init__(self):
        print("This is Tiger class")


newTiger = Tiger()
'''Object of Tiger Class created'''
newTiger.animal_attribute()
'''Object of Tiger Class calling method of Inherited Class'''

'''Q2'''
"""
A B
A B
"""

'''Q3'''
class Cop:
    '''Cop class defined'''
    def __init__(self):
        '''Class initialized with name, age , work experience and designation'''
        self.name = "xyz"
        self.age = 20
        self.work_exp = 0
        self.desg = "-"

    def add(self):
        '''Method to Add the details'''
        self.name = input("Enter the Name: ")
        self.age = int(input("Enter th Age: "))
        self.work_exp = int(input("Enter the Work Experience (in years): "))
        self.desg = input("Enter the Designation: ")

    def display(self):
        '''Method to display the Details'''
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Work Experience: ", self.work_exp)
        print("Designation", self.desg)

    def update(self):
        '''Method to display the Details'''
        self.name = input("Enter the Updated Name: ")
        self.age = int(input("Enter the Updated Age: "))
        self.work_exp = int(input("Enter the Updated Work Experience (in years): "))
        self.desg = input("Enter the Updated Designation: ")


class Mission(Cop):
    '''Mission class defined extending Cop class'''
    def add_mission_details(self, newCop = Cop()):
        '''add_mission_details method'''
        newCop.add()
        newCop.display()
        newCop.update()


newMission = Mission()
newMission.add_mission_details()

'''Q4'''
class Shape:
    '''Creating Shape Class'''
    def __init__(self):
        '''Initializing with Length and Breadth'''
        self.length = "xyz"
        self.breadth = 20

    def area(self):
        '''Defining area method'''
        self.area = self.length * self.breadth


class Rectangle(Shape):
    '''Creating Rectangle Class Inheriting Shape Class'''
    def area(self):
        '''Calculating Area of Rectangle'''
        self.length = int(input("Enter the Length: "))
        self.breadth = int(input("Enter the Breadth: "))
        self.ar = self.length * self.breadth
        print("Area of Rectangle is: ", self.ar)

class Square(Shape):
    '''Creating Square Class Inheriting Shape Class'''
    def area(self):
        '''Calculating Area of Rectangle'''
        self.side = int(input("Enter the Side: "))
        self.ar = self.side * self.side
        print("Area of Square is: ", self.ar)


sq = Square()
sq.area()
rect = Rectangle()
rect.area()