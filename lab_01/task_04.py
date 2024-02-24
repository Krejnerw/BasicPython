first_number = 5
second_number = 2

print(f'or {first_number | second_number}')
print(f'and {first_number & second_number}')
print(f'move left {first_number << second_number}')
print(f'move right {first_number >> second_number}')
print(f'logiczna alternatywa rozłączna {first_number ^ second_number}')
print(f'negacja {~first_number}')

# EX. 1
is_kasia_adult = 1
id_ola_adult = 0
if is_kasia_adult & id_ola_adult:
    print("They can watch together adult movies")
else:
    print("They can not watch together adult movies")

# EX. 2
has_kasia_cookie = 0
has_basia_cookie = 1
if has_kasia_cookie | has_basia_cookie:
    print("Some of them has cookie they can eat")
else:
    print("none of them have cookie they can not eat cookie :C")
# EX. 3
x = 5
y = 2
move_to_left = x << y
print(f'{x} as binary {x:b}')
print(f'move "{y}" to left = {move_to_left} as binary {move_to_left:b}')

# EX. 4
x = 9
y = 2
move_to_right = x >> y
print(f'{x} as binary {x:b}')
print(f'move "{y}" to right = {move_to_right} as binary {move_to_right:b}')

# out of scope
# logiczna alternatywa rozłączna
x = 9
y = 18
result = x ^ y
print(f'{x} as binary {x:b}')
print(f'{y} as binary {y:b}')
print(f'{result} as binary {result:b}')
print(f'{0} as binary {0:b} -> negacja -> {~0} as binary {~0:b}')
print(f'{1} as binary {1:b} -> negacja -> {~1} as binary {~1:b}')
print(f'{9} as binary {9:b} -> negacja -> {~9} as binary {~9:b}')
print(f'{-5} as binary {-5:b} -> negacja -> {~-5} as binary {~-5:b}')
