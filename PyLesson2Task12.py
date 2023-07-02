# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого 
# Петя # делает две подсказки. Он называет сумму этих чисел S и
# их произведение P. Помогите Кате отгадать задуманные Петей числа.
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
num_mul = intNumEnter('Please enter multuply of two numbers: ')
num_sum = intNumEnter('Please enter sum of two numbers: ')

for i in range(1, coins_amount):
    coin = int(random.randrange(0,19)/10)
    print(coin, end=' ' )
    if coin == 0: coins_tail+=1
    if coin == 1: coins_head+=1
print()
if coins_head<coins_tail: 
    print("Coins head are to turn, their amount is: ", 0, "pcs.")
else: 
    print("Coins tail are to turn, their amount is: ", 1, "pcs.")
