'''a prime number i a number that is divisible only by itself and 1 
(e.g. 2, 3, 5, 7, 11) Also , you can think of it as A Prime Number 
is a number that cannot be made by multiplying other whole numbers
'''
def find_primes(num1:int,num2:int):

    for numbers in range(num1,num2+1):
        if numbers > 1:
            for i in range(2,numbers):
                if(numbers % i) == 0:
                    break
            else:
                print(numbers)

find_primes(25,50)



