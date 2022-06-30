
# Gang of Four implementation
class A:
    _instance = None

    def __init__(self):
        raise RuntimeError(f"Please call {__class__.__qualname__}.instance() instead")
    
    @classmethod
    def instance(cls):
        if not cls._instance:
            print(f"Creating new instance of {__class__.__qualname__}")
            cls._instance = cls.__new__(cls)
            # initialise your instance here
        return cls._instance


# Pythonic implementation
class B:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            print(f"Creating new instance of {__class__.__qualname__}")
            cls._instance = super().__new__(cls)
            # initialise here
        return cls._instance


# Usage
# a = A() # raises an error
a1 = A.instance()
a2 = A.instance()
print(f"a1 same as a2: {a1 is a2}")
b1 = B()
b2 = B()
print(f"b1 same as b2: {b1 is b2}")
