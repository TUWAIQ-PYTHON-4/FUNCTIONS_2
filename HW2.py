
def prime_num(first_num:int, second_num:int):
    '''
    This function used to printing prime numbers between two parameter
    '''
    for n in range(first_num, second_num + 1, 1):
        for i in range(2, n, 1):
            if (n % i) == 0:
                break
        else:
            print(n, end=" ")

prime_num(25,50)            

# OUTPUT: 29 31 37 41 43 47