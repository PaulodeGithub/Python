

def make_bold(function):
    def wrapper_function(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<em>{result}</em>"
    return wrapper_function

def make_underline():
 ...

def make_emphasis():
   ...