import time
from functools import wraps

def measure_perfomance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} зроблено за {end_time - start_time:.4f} секунд ")
        return result
    return wrapper
