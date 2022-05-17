



def FindPrimes(n1:int,n2:int):
 for i in range(n1,n2):
    if i > 1:
     for k in range(2,i):
        if (i%k) == 0:
         break
     else:
         print(i)

FindPrimes(25,50) 
