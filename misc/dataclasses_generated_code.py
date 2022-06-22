# !!! 
# This solution relies on the internal 
# implementation of the dataclasses module.
# !!!

import dataclasses
from dataclasses import dataclass

create_fn = dataclasses._create_fn

def my_create_fn(name, args, body, **kwargs):
    locals = kwargs.get('locals')
    def format(arg):
        if ":" in arg:
            n, t = arg.split(":")
            if "=" in t:
                t, d = t.split("=")
                return f"{n}: {locals.get(t).__name__} = {locals.get(d)}"
            return f"{n}: {locals.get(t).__name__}"
        return arg
    
    args_str = ', '.join(format(arg) for arg in args)
    body_str = '\n'.join('  ' + l for l in body)
    print(f'def {name}({args_str}):\n{body_str}\n')
    return create_fn(name, args, body, **kwargs)

dataclasses._create_fn = my_create_fn

# Creating a new dataclass will call my_create_fn
# and output the generated code to stdout
@dataclass
class Person:
    firstname: str
    lastname: str
    age: int = 18

# Inspecting __hash__ directly 
# since the assignment is not performed by calling my_create_fn
print(f"__hash__ = {Person.__hash__}")
