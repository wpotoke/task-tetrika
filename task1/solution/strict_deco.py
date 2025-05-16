from functools import wraps

def strict(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        count = 0
        annotations = func.__annotations__
        for i, type_arg in enumerate(annotations):
            if type_arg not in ['return', 'kwargs', 'args']:
                count += 1
                if not isinstance(args[i], annotations[type_arg]):
                    expected_type = annotations[type_arg]
                    raise TypeError(f"Argument {args[i]} is not of type {expected_type}")
                
        if "args" in annotations:
            expected_type = annotations["args"]
            for i in args[count:]:
                if not isinstance(i, expected_type):
                    raise TypeError(f"Argument {i} is not of type {expected_type}") 
                
        if "kwargs" in annotations:
            expected_type = annotations["kwargs"]
            for i in kwargs.values():
                if not isinstance(i, expected_type):
                    raise TypeError(f"Argument {i} is not of type {expected_type}")
                
        return func(*args, **kwargs)
    return wraper
