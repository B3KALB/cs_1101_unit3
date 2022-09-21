take_a_guess = 13

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
            print(f"{incoming}: You nailed it!")

nest_it_deep(take_a_guess)# og version
# 
# 
take_a_guess_right = 13
take_a_guess_low = 2
take_a_guess_high = 19

# Chained conditionals
def check_it_out(incoming):
    if incoming == 13:
        print(f"{incoming}: You nailed it!")
    elif incoming <= 12:
        print(f"{incoming}: Bit higher!")
    else:
        print(f"{incoming}: Too high!") 

check_it_out(take_a_guess_low)
check_it_out(take_a_guess_right)
check_it_out(take_a_guess_high)

# Nested conditionals

def nest_it_deep(incoming):
    if incoming <= 12:
        print(f"{incoming}: Bit higher!")
    else:
        if incoming >= 14:
            print(f"{incoming}: Too high!")
        else:
            print(f"{incoming}: You nailed it!")

nest_it_deep(take_a_guess_low)
nest_it_deep(take_a_guess_right)
nest_it_deep(take_a_guess_high)

# 
# 
# 
# input version
whole_num = input("Please enter an integer: ")

take_a_guess = int(whole_num)

# Chained conditionals
def check_it_out(incoming):
    if incoming == 13:
        print(f"{incoming}: You nailed it!")
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
            print(f"{incoming}: You nailed it!")

nest_it_deep(take_a_guess)

# RESPONDING CODE
n=int(input("Enter your number: "))

def odd_or_even(n):
    if (n > 0):
        print("Positive")
    else:
        print("Negative")
    if(n%2==0):
        print("even")
    else:
        print("odd")

def number():
    odd_or_even(n)

number()