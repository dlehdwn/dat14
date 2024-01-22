from abc import ABC, abstractmethod

class Shape(ABC):

    def get_area(self):
        pass
    def get_round(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.radius = r

    def get_area(self):
        return 3.14 * self.radius **2
    def get_round(self):
        return 3.14 * self.radius * 2





from abc import ABC, abstractmethod

class Shape(ABC):

    def get_area(self):
        pass
    def get_round(self):
        pass

class T(Shape):
    def __init__(self,hight,lengh):
        self.hight = hight
        self.lengh = lengh

    def get_area(self):
        return self.hight * self.lengh //2
    def get_round(self):
        return self.lengh *3

a = T(3,2)
print(a.get_area())
print(a.get_round())