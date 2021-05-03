import time 

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\nwork time of " + func.__name__ + " : \n" + str((end - start) * 1000) + " mil second\n" )
        return result
    return wrapper


