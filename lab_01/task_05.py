# Note that float.hex() is an instance method, while float.fromhex() is a class method.

some_float = 57.075
some_hex_from_float = float.hex(some_float)
float_from_hex = float.fromhex(some_hex_from_float)
print(f"some_float: {some_float}")
print(f"some_hex_from_float: {some_hex_from_float}")
print(f"float_from_hex: {float_from_hex}")
