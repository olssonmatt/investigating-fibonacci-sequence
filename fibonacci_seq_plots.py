import matplotlib.pyplot as plt
#displays the fibonacci sequence and plots.

def fib(n):
    n1 = 0
    n2 = 1
    count = 0
    r=[0,1]
    while count < n-1:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        r.append(nth)
        count += 1
    return r

fibvalues = fib(30)
print(fibvalues)
plt.plot(fibvalues)
