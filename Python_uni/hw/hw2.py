# hw2
# 作者: 林晏亘
# 用途: 輸入m,n，回傳最大公因數

"""_summary_
    最大公因數(Greatest Common Divisor, 簡稱 GCD)是指兩個或多個整數中共有的最大的因數。
    例如: 12和18的最大公因數是6, 因為它們的公因數有1、2、3和6, 其中最大的是6
"""

m, n = map(lambda x: int(x), input("please input two number, m and n(split by space):").split(" "))
m, n = (m, n) if m > n else (n, m)

# 2.1 用for實作 (function名稱: gcd_for)
def gcd_for(m, n):
    
    """_summary_

    Args:
        m (int): 大數
        n (int): 小數

    Returns:
        int: 回傳m與n的最大公因數
    """
    
    for i in range(n, 0, -1):
        if (m % i) == 0 and (n % i) == 0:
            return i
    

# 2.2 用while實作 (function名稱: gcd_while)
def gcd_while(m, n):
    
    """_summary_

    Args:
        m (int): 大數
        n (int): 小數

    Returns:
        int: 回傳m與n的最大公因數
    """
    
    while n != 0:
        m, n = n, m % n
    return m
    

# 2.3 用遞迴實作 (function名稱: gcd_recursive)
def gcd_recursive(m, n):
    
    """_summary_

    Args:
        m (int): 大數
        n (int): 小數

    Returns:
        int: 回傳m與n的最大公因數
    """
    
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m%n)


print("gcd_for:")
print(gcd_for(m, n))

print("gcd_while:")
print(gcd_while(m, n))

print("gcd_recursive:")
print(gcd_recursive(m, n))