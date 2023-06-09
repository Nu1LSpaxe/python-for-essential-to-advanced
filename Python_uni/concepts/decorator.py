def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # 在執行原始函式之前執行的程式碼
        result = original_function(*args, **kwargs)
        # 在執行原始函式之後執行的程式碼
        return result
    return wrapper_function

@decorator_function
def my_function(x, y):
    pass

#####################################################

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Call function {func.__name__}, params: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} result: {result}')
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

#####################################################

def to_uppercase_decorator(func):
    def wrapper(name):
        return func(name.upper())
    return wrapper

@to_uppercase_decorator
def greeting(name):
    return f"Hello, {name}!"

result = greeting("Eric")
print(result)