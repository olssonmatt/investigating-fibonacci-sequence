import matplotlib.pyplot as plt
#this program calculates the ratio for the current / preceeding
#fib numbers returning a sequence and plots them

def fibratio(n):
    n1 = 0
    n2 = 1
    count = 0
    ratio=[]
    while count < n-1:
        nth = n1+n2
        n1=n2
        n2 = nth
        ratio.append(n2/n1)
        count+=1
    return ratio

ibrvalues = fibratio(1000)
print(fibrvalues)
plt.plot(fibrvalues)

######################################################################
import math
#by solving for the general solution of n
#we are able to obtain the n’th fibonacci number.

def binetformula(n):
    phi = (math.sqrt(5)+1)/2
    fib = ((phi**n)-(-phi**(-n)))/math.sqrt(5)
    return fib

print(binetformula(25))
