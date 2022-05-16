'''
 FUNCTIONS_2

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

#### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between 25 and 50 are:
29   
31   
37   
41   
43   
47   
'''
def find_primes(start_num:int , end_num:int):
   for i in range(start_num,end_num):
          for j in range(2,i):
              if i % j == 0:
                 print(i,"not prime number..")
                 break
          else:
              print(i,"prime number..")
find_primes(25,50)
