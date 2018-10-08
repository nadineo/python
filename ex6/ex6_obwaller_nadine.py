import random
import numpy as np
from random import randint
import sys
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx

def PrimeGen(n=10000):
    primes = []
    chk = 2
    while len(primes) < n:
        ptest = [chk for i in range(2,chk) if chk%i == 0]
        primes += [] if ptest else [chk]
        chk += 1
    return primes

def decrypt(pk, ciphertext):
    plain = []

    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    for i in range(len(ciphertext)):
        try:            
            plain.append(chr((pow(ciphertext[i],key)%n)))

        except OverflowError as e:
            print("except")
            pass
        else:
            pass
        finally:
            pass
    #Return the array of bytes as a string
    return ''.join(plain)
    

def primeFactorization(n):
    p = 0
    q = 0
    #calculate primes from 2 - sqrt(n)
    primes = PrimeGen(math.floor(math.sqrt(n)))

    #find first divisor of n that is prime where n mod p == 0
    #starting at the square root of n
    p_to_find = math.floor(math.sqrt(n))
    isfound = False

    while isfound!= True and p_to_find > 1:
        try:
            idx = primes.index(p_to_find)
            if((n%primes[idx])== 0):
                isfound = True
            else: 
                p_to_find = p_to_find-1
        except Exception as e:
            p_to_find = p_to_find-1
            pass
        else:
            pass
        finally:
           
            pass

    if isfound == True:
        p = p_to_find
        q = n//p
    
    return (p,q)

encrypted_msg = [84620, 66174,66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 
72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 
34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 
9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]

e = 29815
n = 100127

#prime factorization of n
(p,q) = primeFactorization(n)

#check return value
if p != 0 or q != 0:
    phi = (p-1)*(q-1)

    d = multiplicative_inverse(e, phi)

    private = (d, n)

    print(decrypt(private, encrypted_msg))

else:
    print("Invalid n")


