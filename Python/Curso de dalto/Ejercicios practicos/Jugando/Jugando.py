dame_un_numero = input("Dame cualquier número racional: ")
if type(dame_un_numero) == int:
    el_doble = int(dame_un_numero) * 2
    print(f"el doble de tu número es {el_doble}")
else:
    el_doble = float(dame_un_numero) * 2
    str_el_doble = str(el_doble)
    if str_el_doble.endswith(".0"):
        pre_el_doble_entero = str_el_doble.removesuffix(".0")
        el_doble_entero = int(pre_el_doble_entero)
        print(f"el doble de tu numero es {el_doble_entero}")
    else:
        print(f"el doble de tu numero es {el_doble}")


give_me_a_number = input("Give me a rational number: ")
if type(give_me_a_number) == int:
    twice_of = int(give_me_a_number) * 2
    print(f"twice your number is {twice_of}")
else:
    twice_of = float(give_me_a_number) * 2
    str_twice_of = str(twice_of)
    if str_twice_of.endswith(".0"):
        before_twice_int = str_twice_of.removesuffix(".0")
        twice_int = int(before_twice_int)
        print(f"twice your number is {twice_int}")
    else:
        print(f"twice your number is {twice_of}")

print("---------------------------")
