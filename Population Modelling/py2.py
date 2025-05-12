import matplotlib.pyplot as plt
import numpy as np
import sys
lim = 1000
                   
def xrate(x,y):
    return r1*x*(1-x/k1)-a*y*x
def yrate(x,y):
    return b*a*y*x - k2*y

#PARAMS
a = 1 #killrate
b = 2 #birthrate of pred per prey avl
r1 = 600 #birthrate of prey
k1 = 900 #char pop of prey
k2 = 900 #death rate of pred
om = 100

step = 0.0001 
xstep = 0.001 
ystep = 0.001 

#-------
#Start pop vect
inx = 700
iny = 10
#-------
x, y = np.meshgrid(np.linspace(-1, lim,30),  
                   np.linspace(-1, lim,30)) 
u = xrate(x,y)
v = yrate(x,y)
#Normalization
m = np.sqrt(np.power(u,2)+np.power(v,2))
u = u/m
v = v/m
#------

def trajectory(ix,iy):
    u1 = xrate(ix,iy)
    v1 = yrate(ix,iy)
    #step = 0.0001 
    ix = ix + u1*step
    iy = iy + v1*step 
    list1.append(ix)
    list2.append(iy) 
    return
def trajectory_disc(ixd,iyd):
    u2 = xrate(ixd,iyd)
    v2 = yrate(ixd,iyd)
    #xstep = 0.001 
    #ystep = 0.001 
    ixd = ixd + u2*xstep
    iyd = iyd + v2*ystep
    list3.append(ixd)
    list4.append(iyd)
    return 

list1 = [inx,]
list2 =[iny,]
list3 = [inx,]
list4 =[iny,]

trajectory(inx,iny)
trajectory_disc(inx,iny)

n=0
while (list1[-1]>1 and list2[-1]>1 and n<1000000):
    trajectory(list1[-1],list2[-1])
    n+=1

n = 0
while (list3[-1]>1 and list4[-1]>1 and n<1000000):
    trajectory_disc(list3[-1],list4[-1])
    n+=1

#Plotting
fig = plt.figure()
plt.plot(list1,list2)
lx = np.linspace(-1,lim)
plt.plot(lx,r1*(1-lx/k1)/a, color = 'r')
ly = np.linspace(-1,lim)
plt.plot(list([k2/b/a])*len(ly), ly,color = 'g')
plt.quiver(x,y,u,v)
plt.xlim(-1,lim)
plt.ylim(-1,lim)
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.title('Continuous')
fig.savefig('lv-predprey-cont.png')
fig.show()

#--------

fig2=plt.figure()
plt.plot(list3,list4)
lx = np.linspace(-1,lim)
plt.plot(lx,r1*(1-lx/k1)/a, color = 'r')
ly = np.linspace(-1,lim)
plt.plot(list([k2/b/a])*len(ly), ly,color = 'g')
plt.quiver(x,y,u,v)
plt.xlim(-1,lim)
plt.ylim(-1,lim)
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.title('Discrete')
plt.grid(True,linestyle ='-')
fig2.show()

fig2.savefig('lv-predprey-disc.png') 

plt.show()
#fin
