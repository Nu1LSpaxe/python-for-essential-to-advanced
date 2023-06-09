# 類別方法(class method): 
# 可以在不實體化物件的情況下，直接使用類別名稱呼叫該方法

class MyClass:
    
    count = 0
    
    def __init__(self, name):
        self.name = name
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count


#####################################################

# 靜態方法(static method)
# 靜態方法與類別方法的主要差異在於參數: 
#   靜態方法沒有預設參數
#   類別方法的第一個參數通常是cls(代表類別本身)

# 靜態方法通常用來定義與類別無關的一般性方法
# 類別方法通常用來操作類別屬性或在類別層級上的執行操作

class MySecondClass:
    
    # 類別屬性
    class_variable = 10
    
    # 靜態方法
    @staticmethod
    def my_static_method(x, y):
        return x + y
    
    # 類別方法
    @classmethod
    def my_class_method(cls, x, y):
        print("My Second class is:", cls)
        return x + y + cls.class_variable

# 使用靜態方法
result = MySecondClass.my_static_method(1, 2)
print(result)

# 使用類別方法
result = MySecondClass.my_class_method(1, 2)
print(result)