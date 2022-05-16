


def find_primes(start:int, end:int) -> int:
    ''' This function prints prime numbers in a range. A prime number
      cannot be made by multiplying other whole numbers and is only divisible by itself and 1'''
    for num in range(start, end):
       if num > 1:
         for i in range(2, num):
             if (num % i) == 0:
                 break
         else:
            print(num)

find_primes(25,50)
print(find_primes.__doc__)