import matplotlib.pyplot as plt

def fibmod(n,m):
    n1 = 0
    n2 = 1
    count = 0
    r=[0,1]
    while count < n-1:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        r.append(nth%m)
        count += 1
    return r

fibmvalues = fibmod(100,25)
print(fibmvalues)
plt.plot(fibmvalues)
cycle = [0, 1, 1, 2, 3, 5, 8, 13, 1, 14, 15, 9, 4, 13, 17, 10, 7, 17,
4, 1, 5, 6, 11, 17, 8, 5, 13, 18, 11, 9, 0, 9, 9, 18, 7, 5, 12, 17, 9,
6, 15, 1, 16, 17, 13, 10, 3, 13, 16, 9, 5, 14, 19, 13, 12, 5, 17, 2, 19, 1]
print(len(cycle)) #- To find the length of Large cycles