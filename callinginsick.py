# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = input()

sick_days = float(sick_days)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if actually_sick == True and sick_days > 0:

    calling_in_sick = True
    print(calling_in_sick)
    print(sick_days)
elif kinda_sick == True and hate_your_job == True and sick_days > 0:
    calling_in_sick = True
    print(calling_in_sick)
    print(sick_days)
else:
    calling_in_sick = False
    print(calling_in_sick)
    print(sick_days)