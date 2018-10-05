##################################################
# IINI4014 Python for programmers (2018 HØST)
# Nadine Obwaller
# Exercise 1: Finding Prime Numbers
##################################################

import math

primesToFind = 1000
count = 0
number = 2
result = []
isPrime = True

while len(result) < primesToFind:
    for i in range(len(result)):
        # if the analysed number is divisible by another prime number
        # it is no prime number itself
        if number%result[i] == 0:
            isPrime = False;
            break
        # only further check is necessary if the divisor is smaller than
        # the square root of the analysed number
        if result[i] > math.sqrt(number):
            break
    if isPrime:
        result.append(number)
    number += 1
    isPrime = True;


strJoin = "\n".join(map(str,result))
print(strJoin)





    


