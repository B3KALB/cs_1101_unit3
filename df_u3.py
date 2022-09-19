take_a_guess = 6

# Chained conditionals
def check_it_out(incoming):
    if incoming == 13:
        print(f"{incoming}:You nailed it!")
    elif incoming <= 12:
        print(f"{incoming}: Bit highter!")
    else:
        print(f"{incoming}: Too high!") 

check_it_out(take_a_guess)

# Nested conditionals

def nest_it_deep(incoming):
    if incoming <= 12:
        print(f"{incoming}: Bit highter!")
    else:
        if incoming >= 14:
            print(f"{incoming}: Too high!")
        else:
            print(f"{incoming}:You nailed it!")

nest_it_deep(take_a_guess)