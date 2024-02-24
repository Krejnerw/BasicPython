some_list = [0.3, 5., 27.0, 1.5]
for i in some_list:
    if float.is_integer(i):
        print(f"Yeah {i} can be {int(i)}")
        print(f"and it has '{int.bit_count(int(i))}' ones as a binary number")
