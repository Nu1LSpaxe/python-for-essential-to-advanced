# hw1
# 作者: 林晏亘
# 用途: 輸入n, 印出n!三角形, 要用function包起來

"""_summary_
    輸入n, 印出n!三角形, 要用function包起來
    例如: 輸入5, 印出結果
    1 
    1 2 
    1 2 6 
    1 2 6 24 
    1 2 6 24 120 

    Returns:
        _type_: _description_
"""

n = int(input("Please input a number n: "))

# 1.1 用for實作
def factorial_triangle_for(n):
    
    """_summary_
    1.1 用for實作 (function名稱: factorial_triangle_for)
    
    Args:
        n (int): 階層數
        
    Returns:
        無回傳值，直接打印
    """
    
    result = 1
    lis = []
    if n == 0 or n == 1:
        print(result); return
    for i in range(1, n+1):
        result *= i
        lis.append(result)
        print(" ".join(map(lambda x: str(x), lis)))


# 1.2 用while實作
def factorial_triangle_while(n):
    
    """_summary_
    1.2 用while實作 (function名稱: factorial_triangle_while)
    
    Args:
        n (int): 階層數
    
    Returns:
        無回傳值，直接打印
    """
    
    result = 1
    lis = []
    i = 1
    if n == 0 or n == 1:
        print(result); return
    while n > 0:
        result *= i
        lis.append(result)
        print(" ".join(map(lambda x: str(x), lis)))
        n, i = n-1, i+1


# 1.3 用遞迴實作
lis = []
def factorial_triangle_recursive(n):
    
    """_summary_
    1.3 用遞迴實作 (function名稱: factorial_triangle_recursive)
    
    Args:
        n (int): 階層數
    
    Returns:
        int: 回傳階層乘數
    """
    
    global lis
    if n == 0 or n == 1:
        lis.append(1)
        print(1)
        return 1
    else:
        result = n * factorial_triangle_recursive(n-1)
        lis.append(result)
        print(" ".join(map(lambda x: str(x), lis)))
        return result
    

print("factorial_triangle_for:")
factorial_triangle_for(n)

print("factorial_triangle_while:")
factorial_triangle_while(n)

print("factorial_triangle_recursive:")
factorial_triangle_recursive(n)
