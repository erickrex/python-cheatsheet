# GENERIC
# example of a generic decorator
from functools import wraps


def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result
    # Return the decorated function
    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))


# COUNTER
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return wrapper.count
    wrapper.count = 0
    # Return the new decorated function
    return wrapper

# Decorate foo() with the counter() decorator


@counter
def foo():
    print('calling foo()')


foo()
foo()

print('foo() was called {} times.'.format(foo.count))


# WRAPS EXAMPLE


def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)


# previously built @checkeverything decorator
def check_everything(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        check_inputs(*args, **kwargs)
        result = func(*args, **kwargs)
        check_outputs(result)
        return result
    return wrapper


@check_everything
def duplicate(my_list):
    """Return a new list that repeats the input twice"""
    return my_list + my_list


t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

# Decorators with arguments


def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

    run_five_times = run_n_times(5)
# Same as


@run_five_times
def print_sum(a, b):
    print(a + b)


print_sum(4, 100)


# Decorator to add either italics or bold
def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)
        # Return the decorated function
        return wrapper
    # Return the decorator
    return decorator

    @html("<div>", "</div>")
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))


print(hello_goodbye('Alice'))


#######
# REAL EXAMPLE OF TIMEOUT IMPLEMENTATION USING DECORATORS
######
def tag(*tags):
    # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    # Return the new decorator
    return decorator


@tag('test', 'this is a tag')
def foo():
    pass


print(foo.tags)


# ASSERTION ERRORS
def returns_dict(func):
    # Complete the returns_dict() decorator
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        assert type(result) == dict
        return result
    return wrapper


@returns_dict
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')


# MORE ON ASSERTION ERRORS
def returns(return_type):
    # Write a decorator that raises an AssertionError if the
    # decorated function returns a value that is not return_type
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert type(result) == return_type
            return result
        return wrapper
    return decorator


@returns(dict)
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')
