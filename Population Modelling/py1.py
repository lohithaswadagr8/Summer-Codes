import matplotlib.pyplot as plt
import numpy as np
import sys
lim = 300
                   
def xrate(x,y):
    return r1*x*(1-(x+a*y)/k1)
def yrate(x,y):
    return r2*y*(1-(y+b*x)/k2)

#params
r1 = 1
r2 = 0.5
a = 0.8 #alpha12
b = 2 #alpha21
k1 = 200
k2 = 300

step = 0.0001 
xstep = 0.001 
ystep = 0.001 

#input
inx = 70
iny = 175
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
    #step = 1 
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
    ixd = np.floor(ixd + u2*xstep)
    iyd = np.floor(iyd + v2*ystep)
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
while (list1[-1]>1 and list2[-1]>1 and n<1000000000000):
    trajectory(list1[-1],list2[-1])
    n+=1

n = 0
while (list3[-1]>1 and list4[-1]>1 and n<1000000):
    trajectory_disc(list3[-1],list4[-1])
    n+=1

#Plotting
fig = plt.figure()
plt.plot(list1,list2)
plt.plot(np.linspace(-1,lim),(k1-np.linspace(-1,lim))/a, color = 'r')
plt.plot((k2-y)/b, y,color = 'g')
plt.quiver(x,y,u,v)
plt.xlim(-1,lim)
plt.ylim(-1,lim)
plt.xlabel('Species 1')
plt.ylabel('Species 2')
plt.title('Continuous')
fig.savefig('lv-predprey-70-175.png')
fig.show()

'''#Plotting again
fig2=plt.figure()
plt.plot(list3,list4)
plt.plot(np.linspace(-1,lim),(k1-np.linspace(-1,lim))/a, color = 'r')
plt.plot((k2-y)/b, y,color = 'g')
plt.quiver(x,y,u,v)
plt.xlim(-1,lim)
plt.ylim(-1,lim)
plt.xlabel('Species 1')
plt.ylabel('Species 2')
plt.title('Discrete')
plt.grid(True,linestyle ='-')
fig2.show()

fig2.savefig('Cont-3.png')'''

plt.show()

#fin
