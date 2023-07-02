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
coins_tail, coins_head, coins_amount = 0, 0, 0
coins_amount = intNumEnter('Please enter coins amount: ')
for i in range(1, coins_amount):
    coin = int(random.randrange(0,19)/10)
    print(coin, end=' ')
    if coin == 0: coins_tail+=1
    if coin == 1: coins_head+=1
print()
if coins_head<coins_tail: 
    print("Coins head are to turn, their amount is: ", coins_head, "pcs.")
else: 
    print("Coins tail are to turn, their amount is: ", coins_tail, "pcs.")
