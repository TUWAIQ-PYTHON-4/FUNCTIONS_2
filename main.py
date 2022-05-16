
def number(val1:int , val2:int  ):

  for i in range(val1,val2+1):
    if i > 1:
        for j in range(2,i):
           if (i%j)==0:
             break
    else:  
            print (i)  

   
  number(10,20)


