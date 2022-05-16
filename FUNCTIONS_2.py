'''

a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers

for example, primes between 25 and 50 are:
29
31
37
41
43
47

'''

def find_primes():
    first_param =int(input("Enter the first number :"))
    second_param=int(input("Enter the second number: "))

    for num in range(first_param , second_param+1):
        if num > 1:
            for i in range(2,num):
                if (num % i )== 0:
                    break
            else:
               print(num)

find_primes()