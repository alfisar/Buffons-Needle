import math
import random

print('N : ', end='')
n = int(input())
print('L : ', end='')
l = float(input())
print('D : ', end='')
d = float(input())

q = 0

for i in range(1,n):
    x = random.uniform(0,d)
    teta = random.uniform(0,90)
    temp = l*math.cos(math.radians(teta))
    if x <= temp:
        q += 1

pi = (n/q) * ((2*l)/d)
print(pi)