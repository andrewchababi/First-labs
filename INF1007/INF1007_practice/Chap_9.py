import numpy as np
import random
import matplotlib.pyplot as plt
import math


"""A = np.array([[-2, -1], [4,1], [-1, -1]])
#print(A.shape)
#print(A)
solved = np.linalg.pinv(A)
b = np.array([[-2],[-8],[-2]])
print(solved )

a = np.array(object=[1,2,3,4,5], dtype= float)
for e in a :
    print(e*2)"""
    
#1 cree un array presentant 64 valeurs uniformement repartie entre -1.3 et 2.5

num_1 = -1.3 
num_2 = 2.5
diff = (num_2-num_1)/64 
vec = [num_1 + i*diff for i in range(64)]
#print(vec)


libtest = (np.linspace(num_1,num_2, num= 64))
#print(libtest)

#2 cree un programme qui calcule la valeur de pi par la methode de montecarlau
 
square_matrix = np.array([[np.random.randint(0,1)] for i in range(3)])
#print(square_matrix)                                                        #fail


n = 100000000

#lib way 
x = np.random.random(n)
y = np.random.random(n)
distance = np.sqrt(x**2 + y**2)
in_circle = distance <= 1
print(in_circle)
pi = (4* (np.count_nonzero(in_circle)))/n
print(pi)

"""
#hardcoding way
x = [random.uniform(a=0, b=1) for _ in range(n)]
y = [random.uniform(a=0, b=1) for _ in range(n)]

counter = 0 
for i in range(n):
    xi, yi = x[i] , y[i]
    if math.sqrt(xi**2 + yi**2) <= 1 :
        counter += 1

print(4*counter / n)
"""

plt.figure(figsize=(5, 5))
plt.scatter(x,y)
plt.tight_layout()
plt.show()




