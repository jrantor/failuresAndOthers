from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Function is not running"
        return f(*args,**kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run=True
