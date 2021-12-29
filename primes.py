import math

from random import randrange, getrandbits

#############################################################################################################################################

#https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
def primeOdds(base,n): # PI(2,1024)
    return 1/math.log(base**n)
    #math.log(base**n)]

#############################################################################################################################################

def is_prime(n, k=128): # > #is_prime(19)  #Uses Miller-Rabin
    # This function Tests if a number (n) is prime, by doing (k) tests (more tests mean more accuracy)
    # It returns True if n is prime

    if n == 2 or n == 3: # n = 2,3 are prime but (they don't pass the test?)  >#(19==2 and 19==3 == False)
        return True
    if n <= 1 or n % 2 == 0: # even numbers or numbers below or equal to 1 can't be primes  >#(19<=1 && 19%%2 == False)
        return False

    # find r and s
    s = 0  # s is initialized with the value 0
    r = n-1 # r is initialized with the value n-1  >#(18)

    while r & 1 == 0:  # while r is even: ( r & 1 returns the less signiticant digit of a binary number)  >#( 18 & 1 == 0 )  >##( 9 & 1 == 1 )
        s += 1  # adds 1 to s  >#(s = 1)
        r //= 2  # does a floor division  >#( r = 18 //= 2  = 9 )

    for _ in range(k):  # does k tests ( _ means that we don't care about the number that it is on the range, we just care about the number of iterations )
        a = randrange(2, n-1)  # a = random number between 2 and n1  >#( random number between 2 and 18 == 3 )
        x = pow(a, r, n)  # x = a^r % n  >#( x = 3^9 % 11  =  19683 % 11  = 4 )
        if x != 1 and x != n - 1:  #  >#( 4!=1 and 4!=18)
            j = 1
            while j < s and x != n - 1:  #  >#( 1<1 and 4!=18 )
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:  #  >#( 4!=18 )
                return False
    return True

#############################################################################################################################################

def generate_prime_candidate(length):
    # Returns a random odd integer with the length in bits being (length)

    # generate random bits
    p = getrandbits(length)

    # apply a mask to set MSB (most significant bit) and LSB (less significant bit) to 1, so that it actually has the length needed (else 0110 would have length 4) and it's odd (x...1 binary numbers are odd)
    p |= (1 << length - 1) | 1
    return p

#############################################################################################################################################

def generate_prime_number(length):
    # Returns a random prime number with the length in bits being (length)

    p = 4

    while not is_prime(p, 128):  # keep generating a random odd integer with length (length) while the primality test fails
        p = generate_prime_candidate(length)
    return p