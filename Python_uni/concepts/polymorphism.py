# 多型(polymorphism)
# 同一個方法可以被不同型別的物件所呼叫，產生不同的行為

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("汪汪")
    
class Cat(Animal):
    def make_sound(self):
        print("喵喵")

def make_animal_sound(animal):
    animal.make_sound()

my_dog = Dog()
my_cat = Cat()

make_animal_sound(my_dog)
make_animal_sound(my_cat)