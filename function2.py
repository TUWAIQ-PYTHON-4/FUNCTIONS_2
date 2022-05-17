def find_primes(num1:int,num2:int):
 
 for i in range(num1,num2):
   
    if i > 1:
     for j in range(2,i):
        if (i%j) == 0:
         break
     else:

         print(i)

find_primes(25,50)