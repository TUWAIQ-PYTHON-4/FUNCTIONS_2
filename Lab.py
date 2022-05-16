def  find_primes(num1:int, num2:int):
 array=range(num1,num2)
 prime=[]
 for i in array:
    for x in range(2, i):
       if not i%x:
          break
    else:
     print(i)
find_primes(25,50)