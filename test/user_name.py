# import random
#
# name = f"User{random.randrange(1,1000)}"
# print(name)

import random

user = "User"                        # Имя
number = random.randrange(1,1000)    # Случайное число
name = user + str(number)            # Случайное имя
print(name)
