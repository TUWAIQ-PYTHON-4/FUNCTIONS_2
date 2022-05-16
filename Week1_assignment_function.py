# FUNCTIONS_2

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

#### hint
# a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
# Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers

def find_primes(min:int,max:int):
    '''
    The find_prime function takes 2 integer parameters and prints the prime numbers between them
    '''
    for i in range(min, max+1): 
    # deviding the i all the numbers between i and j to find the prime numbers 
        for j in range(2,i): 
            if (i%j) == 0:
             break
        else: 
          print(i)



find_primes(10,20)