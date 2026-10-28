import time
from functools import wraps

def advanced_memoize(ttl_seconds):
    def decorator(func):
        cache = {}
        @wraps(func)
        def wrapper(*args):
            current_time = time.time()
            if args in cache:
                result, timestamp = cache[args]
                if current_time - timestamp < ttl_seconds:
                    return result
            result = func(*args)
            cache[args] = (result, current_time)
            return result
        return wrapper
    return decorator
