# Задача 14:
# Требуется вывести все целые степени двойки (т.е.
# числа вида 2k), не превосходящие числа N.
def intNumEnter(msg=''):
    num_str = '0'
    num = 0
    run_again = True
    while run_again:
        num_str = input(msg)
        if num_str.isdigit(): 
            num = int(num_str)
            run_again = False if num >= 0 else True
    return num
# random.seed(a=None, version=2)
num_degree = intNumEnter('Please enter "N" number: ')
i, num2 = 0, 1
while num2 <= num_degree:
    print('The value of number "2" in degree "', i ,' is: "', num2)
    i +=1
    num2 = num2 * 2
