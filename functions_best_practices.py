import time


def timer(func):
    """Define the wrapper function to return"""
    # Define the wrapper function to return
    def wrapper(*args, **kwargs):
        # When wrapper() is called, get the current time
        t_start = time.time()
        # Call the decorated function and store the result
        result = func(*args, **kwargs)
        # Get the total time it took to run and print it
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
        return result
    return wrapper


@timer
def sleep_n_seconds(n):
    time.sleep(n)


sleep_n_seconds(2)


def memoize(func):
    """Store the results of the decorated function for fast lookup"""
    # Store results in a dict that maps arguments to results
    cache = {}
    # Define the wrapper function to return

    def wrapper(*args, **kwargs):
        # If these arguments have not been seen before
        if (args, kwargs) not in cache:
            # Call func() and store the result
            cache[(args, kwargs)] = func(*args, **kwargs)
        return cache[(args, kwargs)]
    return wrapper


@memoize
def slow_function(a, b):
    print('Sleeping...')
    time.sleep(5)
    return a + b


slow_function(3, 4)
