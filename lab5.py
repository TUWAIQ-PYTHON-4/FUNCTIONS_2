
def primes(num1:int, num2:int):
    for x in range(num1, num2):
     for i in range(2, x):
      if (x % i) == 0:
        break
     else:
         print(x)
                
            
primes(25,50)

