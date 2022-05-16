# FUNCTIONS_2
def find_primes(num_1:int,num_2:int) -> int:
    '''
    a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
    Also , you can think of it as A Prime Number is a number that cannot be made by multiplying
    other whole numbers
    '''
    for number in range (num_1, num_2):    
              for i in range (2, number):  
                  if number % i == 0:  
                      break  
              else:
                  print(number)             

find_primes(25,50)
