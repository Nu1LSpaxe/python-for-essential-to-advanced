class Dog:
    name = 'dog'
    hobby = 'eat'
    ears = 2
    legs = 4
    
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby
    
    
    # 若沒有__str__, 則會印出__main__.Dog object at 記憶體區塊
    # 若有, 則print() 會出現__str__中的內容
    def __str__(self):
        return f"Dog: {self.name}"

my_pet = Dog('Dok', 'destory everything')

print(my_pet)

#####################################################

class Cat:
    name = 'cat'
    hobby = 'sleep'
    ears = 2
    legs = 4
    
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby
        
class Kitty(Cat):
    def __init__(self):
        self.age = 12
        # 利用super()調用父類別的__init__()
        # super()不需要再傳入self
        super().__init__('Kitty', 'eat')

my_cat = Kitty()
print(my_cat.age, my_cat.name, my_cat.hobby)
