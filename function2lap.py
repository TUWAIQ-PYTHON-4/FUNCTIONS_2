def primeNumber(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def primeBetween(start,end):
    for i in range(start , end):
        if primeNumber(i):
            print(i)

primeBetween(25 , 50)