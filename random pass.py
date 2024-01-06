import random

def password_generator(number_characters):
        str_forward=""
        str_backward=""
        character=""
        for forward in range(1,number_characters+1):
            str_forward+=str(forward)
        for backward in range(1,number_characters+1):
            str_backward+=str(backward)

        return random.randrange(int(str_forward),int(str_backward[::-1]))
while True:
    try:
        number_characters=int(input("Length of password: "))
        if number_characters<4:
            raise Exception
    except (Exception,ValueError):
        print('Not In Range please  A Try Number')
    else:
        print(password_generator(number_characters))
        break

