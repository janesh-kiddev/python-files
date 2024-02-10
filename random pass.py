import random


string = "PASSWORD WITH NUMBERS"
new_string = string.center(25, '$')
print(new_string)


def password_generator(number_characters):
        str_forward = ""
        str_backward = ""
        for forward in range(1,number_characters+1):
            str_forward += str(forward)
        for backward in range(1,number_characters+1):
            str_backward += str(backward)

        return random.randrange (int(str_forward),int(str_backward[::-1]))

while True:
    try:
        number_characters = int(input("Set the length of password greater than 4 and less than 16: ").title())
        if number_characters < 4:
            raise Exception
        if number_characters > 16:
            raise Exception
    except(Exception,ValueError):
        print('Please a Try Number')
    else:
        val = str(password_generator(number_characters))
        print(f"THE PASSWORD IS {val}")
        break


