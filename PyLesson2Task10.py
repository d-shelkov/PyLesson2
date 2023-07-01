# Lesson 2, task 10
import random
def intNumEnter(msg=''):
    num_str = '0'
    num = 0
    run_again = True
    while run_again:
        num_str = input(msg)
        if num_str.isdigit(): 
            num = int(num_str)
            run_again = False if num > 0 else True
    return num

# random.seed(a=None, version=2)
coins_tail, coins_head, coins_amount = 0
coins_amount = intNumEnter('Please enter coins amount: ')
for i in range(1, coins_amount):
    coin = random(0,1)
    print(coin, end=' ' )
    if coin == 0: coins_tail+=1
    if coin == 1: coins_head+=1
print(coins_head if coins_head<coins_tail else coins_tail)