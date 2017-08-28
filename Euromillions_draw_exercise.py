# EXERCISE: EUROMILLIONS DRAW
# (using itertools)


# Rules of EuroMillions for lottery ticket numbers:
# 5 numbers from 1 to 50
# 2 star numbers from 1 to 12 (which can be a repeat from previous 5)

# we want to create a function that generates randomly such numbers

# FIRST VERSION (with calculated n combinations):
# for numbers from 1 to 50,
# in theory I can have 2118760 combinations of 5 numbers [50!/(5!*45!)]
# for numbers from 1 to 12,
# in theory I can have 66 combinations of 2 numbers [12!/(2!*10!)]

import random
import itertools

def gen_lotto_selection():
    n =random.randint(1, 2118760)
    my_list = list(range(1, 51))
    comb_list_5 = list(itertools.combinations(my_list, 5))
    lotto_5 = comb_list_5[n]
    print('My first numbers are:', lotto_5)
    s = random.randint(1, 66)
    my_star_list = list(range(1, 13))
    comb_list_2 = list(itertools.combinations(my_star_list, 2))
    lotto_stars = comb_list_2[s]
    print('My star numbers are:', lotto_stars)
    print('My full lotto combination is: first 5 numbers', lotto_5, 'with star numbers', lotto_stars)


# or
# if I don't want to calculate max number of n before
# and I want instead to determine it inside with 'len'

import random
import itertools

def gen_lotto_selection2():
    my_list = list(range(1, 51))
    comb_list_5 = list(itertools.combinations(my_list, 5))
    n_max=len(comb_list_5)
    n = random.randint(1, n_max)
    lotto_5 = comb_list_5[n]
    print('My first numbers are:', lotto_5)
    my_star_list = list(range(1, 13))
    comb_list_2 = list(itertools.combinations(my_star_list, 2))
    s_max=len(comb_list_2)
    s = random.randint(1, s_max)
    lotto_stars = comb_list_2[s]
    print('My star numbers are:', lotto_stars)
    print('My full lotto combination is: first 5 numbers', lotto_5, 'with star numbers', lotto_stars)