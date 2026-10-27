import functools
import time


def log(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(level + ", " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ", " + func.__name__)
            result = func(*args, **kwargs)
            print(level + ", " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ", " + func.__name__)
            return result

        return wrapper

    return decorator


# @log(level='Info')
def add(x, y):
    print("add two numbers: {} and {}".format(x, y))
    return x + y


f = log('Info')(add)
print(f.__name__)
r = f(1, 2)
print(r)
