# Lesson 2, task 10
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
coins_amount = 0
coins_amount = intNumEnter('Please enter coins amount: ')
for i in range(1, coins_amount):
    