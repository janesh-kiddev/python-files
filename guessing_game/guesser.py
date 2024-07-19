import random
print("#####Guesses#####".center(100))
print("This is a game where the task is find the number within 10 tries".title())

thrsh = int(input("set threshold for finding the value:").title())

real_number = random.randint(0,thrsh)
tries = 10

c = 0

while True:
    if c == tries:
        print(f"TRY AGAIN NEXT TIME the number was {real_number}")
        break
    
    c+=1
    find = int(input(f'find the number:'))
    if find == real_number:
        print(f"found at {c} tries the number is {real_number}")
        break
    
    elif real_number > find:
        print('The number is larger')
    
    elif real_number < find:
        print('The number is lower')
