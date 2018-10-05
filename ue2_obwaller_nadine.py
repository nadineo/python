##################################################
# IINI4014 Python for programmers (2018 HØST)
# Nadine Obwaller
# Exercise 2: Estimation of PI with archimedes
##################################################

from decimal import Decimal, getcontext

def pi_calculation(it):
    # pi is calculated by the algorithm of archimedes in it iterations
    poly_sides = 2
    poly_square_edge = Decimal(2)
    for i in range(it):
        poly_square_edge = 2 - 2 * (1 - poly_square_edge / 4).sqrt()
        poly_sides *= 2
    return poly_sides * poly_square_edge.sqrt()

#calculation 
places = 100
last_res = None
for i in range(10*places):
    #following calc with double prec
    getcontext().prec = 2*places
    res = pi_calculation(i)
    #print with single prec
    getcontext().prec = places
    res = +res
    print("%3d: %s\n" % (i, res))
    #calculation is finished if last result is equal to current result
    if res == last_res:
        break;
    last_res = res


