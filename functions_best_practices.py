import signal
import time
from functools import wraps


def timer(func):
    """Define the wrapper function to return"""
    # Define the wrapper function to return
    @wraps(func)
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


# @timer
# def sleep_n_seconds(n):
#     time.sleep(n)


# sleep_n_seconds(2)


def memoize(func):
    """Store the results of the decorated function for fast lookup"""
    # Store results in a dict that maps arguments to results
    cache = {}
    # Define the wrapper function to return

    @wraps(func)
    def wrapper(*args, **kwargs):
        # If these arguments have not been seen before
        key = (args, tuple((kwargs.items())))
        if key not in cache:
            # Call func() and store the result
            cache[key] = cc = func(*args, **kwargs)
            return cc
        return cache[key]
    return wrapper


@memoize
def slow_function(a, b):
    print('Sleeping...')
    time.sleep(5)
    return a + b


print(slow_function(3, 4))

print("memoized below")
print(slow_function(3, 4))


def raise_timeout(*args, **kwargs):
    raise TimeoutError()


# When an alarm signal goes off, call raise_timeout
signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)

# Set off an alarm in 5 seconds
signal.alarm(5)
# Cancel the alarm
signal.alarm(0)


def timeout_in_5s(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Set an alarm for 5 seconds
        signal.alarm(5)
        try:
            # Call the decorated func
            return func(*args, **kwargs)
        finally:
            # Cancel alarm
            signal.alarm(0)
    return wrapper


@timeout_in_5s
def foo():
    time.sleep(10)
    print('foo!')

# DECORATOR FACTORY


def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Set an alarm for n seconds
            signal.alarm(n_seconds)
            try:
                # Call the decorated func
                return func(*args, **kwargs)
            finally:
                # Cancel the alarm
                signal.alarn(0)
        return wrapper
    return decorator


@timeout(5)
def foo():
    time.sleep(10)
    print('foo!')


@timeout(20)
def bar():
    time.sleep(10)
    print('bar!')
