
def is_prime(n):
    '''
    this function check is it prime or not.
    :param n: intger
    :return: boolean
    '''
    # any number less thane or = 1 is not prime
    if (n <= 1):
        return False

    # Check from 2 to n
    for i in range(2, int(n)):
        if (n % i == 0):
            return False

    return True

def  find_primes(num1, num2):
    '''
    this function takes the two integers and then the method is_prime() is called 
    which returns True if the number is prime and False otherwise.
    '''
    for i in range(num1, num2):
         if is_prime(i):
           print(i)


find_primes(25,50)
