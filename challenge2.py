'''
@Author: Shweta Medhekar
@Created Date: March 2011
'''

import sys
import math

def calcFib(n1,n2):
    ''' This function generates the next Fibonacci number '''
    next_n=n1+n2
    return next_n

def checkPrime(n):
    ''' This function checks if a number is prime or not. It returns True or False'''
    root = int(math.sqrt(n))+1
    isPrime="True"
    if(n>2):    
        for i in range (2,(root+1)):
            if(n % i == 0):
                isPrime="False"
                break
    return isPrime

def getFactors(n):
    ''' This function returns all the factors for a given number'''
    factors=[]
    i=2
    while(n>1):
       while(n % i == 0):
           n = n/i
           factors.append(i)
       i=i+1
    return factors


def main():
    input_val=227000 #defined input value
    n1=0
    n2=1
    next_n=n2

    while(True):
        next_n=calcFib(n1,n2)
        n1=n2
        n2=next_n
        # This checks for the required condition
        if((next_n > input_val) and (checkPrime(next_n)=='True')):
            output_val=next_n
            break

    # Step 1
    print "Input value : ",input_val
    print "Required Prime : ",output_val

    # Input to Step 2
    next_step=output_val+1
    print "Input for the next step : ",next_step

    factors = getFactors(next_step)
    # This removes all the duplicates
    factors = list(set(factors))
    print factors

    # Get just the prime factors
    i = 0
    while(i < len(factors)):
        if(checkPrime(factors[i])=='False'):
            factors.pop(i)
        else:
            i=i+1
    
    print 'Factors: ',factors

    sum=0
    for i in range(0,len(factors)):
        sum=sum+factors[i]

    print 'Sum: ', sum

if __name__ == "__main__":
    sys.exit(main())
