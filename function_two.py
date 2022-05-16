'''
Create a function : find_primes that takes in 2 parameters of type int , 
and print the prime numbers between the first parameter and the second parameter .
hint: a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)
'''

def find_primes(num1: int, num2: int):
    lst= range(num1,num2+1)
    for num in lst:
        #check if number is divisable by 2 up to the number itself (exclusive).
        for divider in range(2,num):
            if num % divider == 0: # not prime
                break
        else:
            print(num)

# calling the function to find prime numbers between 25 and 50.
find_primes(25,50)