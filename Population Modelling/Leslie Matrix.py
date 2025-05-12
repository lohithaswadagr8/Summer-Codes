import matplotlib.pyplot as plt
import numpy as np
les_mat = [[0.4,3],[0.32,0.7]]
pop_vect = [200,0]
a = int(sum(pop_vect))
b = 1000
t = b/a
l = []
l1 = []
l2 = []
n = 0

while abs(t)>=0.0000000000000000001:
    
    n_1_vect = pop_vect
    pop_vect = np.dot(les_mat,pop_vect)
    a1 = a
    b1 = b
    a = sum(pop_vect)
    b = sum(n_1_vect)
    l1.append(a1)
    l2.append(n)
    n +=1
    l.append(a/b)
    t = b1/a1-b/a
print(l)
print(a1/b1, ' is the ratio of populations at two consecutive timesteps.')
plt.plot(l2,np.log(l1))
plt.show()
