# 封裝(Encapsulation)
# 把物件內部的資料和方法包裝在一起，對外界隱藏物件的內部實現細節
# 僅向外界提供必要接口，只能透過這些接口訪問物件內部狀態

# 隱藏敏感資訊、防止誤改、隔離不同模組

# 使用單個底線(_): 受保護，外界可以訪問但不建議直接訪問
# 使用雙個底線(__): 私有，外部無法直接訪問

class Car:
    def __init__(self, color):
        self.__color = color
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

my_car = Car('black')
print(my_car.get_color())

my_car.set_color('red')
print(my_car.get_color())


#####################################################

# @property
# 該裝飾器可以將一個方法轉換為一個屬性(可以直接存取屬性而非調用方法)
# @屬性名.setter 可以將原來的setter方法轉為屬性的setter方法
# @property裝飾器的getter方法不需要使用self參數(被當屬性而非方法)

class Truck:
    def __init__(self, color):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

my_truck = Truck('black')
print(my_truck.color)

my_truck.color = 'red'
print(my_truck.color)


#####################################################

# 特殊方法(special method)
# __init__(self, ...): 用來初始化類別的屬性或方法; 當一個對象被創建時，init()方法會被自動調用
# __str__(self): 定義對象被轉換為字串時應該返回的值
# __len__(self): 定義當使用len()函數時應該返回的值
# __delitem__(self, key): 定義當使用del關鍵字刪除對象時應該如何處理

# 比較器(Comparator)用來比較物件之間大小的方法
# __eq__(self, other): ==
# __ne__(self, other): !=
# __lt__(self, other): <
# __gt__(self, other): >
# __le__(self, other): <=
# __ge__(self, other): >=

# 沒有定義則無法實現功能
