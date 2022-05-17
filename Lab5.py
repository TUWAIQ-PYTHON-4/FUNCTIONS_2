def find_primes(num1:int , num2:int):
    '''
    This function prints only the prime numbers 
    between the two parameters entered
    '''

    print("Prime numbers between", num1, "and", num2, "are:")

    for i in range(num1, num2 + 1):

        if i > 1:
        # all prime numbers are greater than 1
            for j in range(2, i):
                # check for factors

                if (i % j) == 0:
                    # not a prime number so break inner loop and
                    # look for next number
                    break
            
            else:
              print(i)


find_primes(1,11)

