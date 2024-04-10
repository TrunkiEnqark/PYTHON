import json

def encode_complex(object):
    if isinstance(object, complex):
        return [object.real, object.imag]
    raise TypeError(repr(object) + " is not JSON serialized")

complex_obj = json.dumps(4 + 9j, default=encode_complex)
print(complex_obj)