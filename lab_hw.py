def find_primes(a,b):
    for num in range(a, b + 1):
     if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

find_primes(25,50)