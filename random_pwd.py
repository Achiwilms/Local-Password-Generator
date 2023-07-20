import random
import string

# Setting

# symbol initialization
symbol = "@#$!%^&*()[]{=}+-*~"

# password length
pwd_len = 20;

# options
add_uppercase = False;
add_lowercase = True;
add_number = True;
add_symbol = False;

# password initialization
pwd = "";

# option list
option_list = [add_uppercase, add_lowercase, add_number, add_symbol]

# options with "True" value
true_option = [index for index, value in enumerate(option_list) if value]

# password generation
for i in range(pwd_len):
    # option 
    option = random.choice(true_option)
    match option:
        # 0 -> uppercase
        case 0:
            pwd += random.choice(string.ascii_uppercase)
        # 1 -> lowercase
        case 1:
            pwd += random.choice(string.ascii_lowercase)
        # 2 -> number
        case 2:
            pwd += str(random.randint(0, 9))
        # 3 -> symbol
        case 3:
            pwd += random.choice(symbol)
        case _:
            raise Exception("Invalid option!")
        
print(f"Password: {pwd}")