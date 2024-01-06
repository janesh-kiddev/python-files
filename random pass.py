import random

def password_generator(number_characters):
    si="asfss"
    sj="ards"
    for i in range(1,number_characters+1):
        si+=str(i)
    for j in range(1,number_characters+1):
        sj+=str(j)

    print(random.randrange(int(si),int(sj[::-1])))

number_characters=int(input("Length of password: "))
password_generator(number_characters)
