import matplotlib.pyplot as plt
import numpy as np

lim = 35
                   
def xrate(x,y):
    return r1*x-a*y*x
def yrate(x,y):
    return -d2*y +g*a*x*y

#PARAMS
a = 0.1 #deathrate of prey per prey and pred avl
r1 = 1.05 #birthrate of prey
g = 0.45 #no pred born per prey dead
d2 = 0.6 #death rate of pred

h = 0.0001
#hrec = 1/h
'''xstep = 0.001 
ystep = 0.001 '''

#-------
#Start pop vect
inx = 30
iny = 10
#-------
x, y = np.meshgrid(np.linspace(-1, lim,20),  
                   np.linspace(-1, lim,20)) 
u = xrate(x,y)
v = yrate(x,y)
#Normalization
m = np.sqrt(np.power(u,2)+np.power(v,2))
u = u/m
v = v/m
#------
nh = 0
switch  = 0
#rung-kutta 4 trajectory
def trajectory(ix,iy):
    kx1 = xrate(ix,iy)
    ky1 = yrate(ix,iy)
    kx2 = xrate(ix+h*kx1/2,iy+h*ky1/2)
    ky2 = yrate(ix+h*kx1/2,iy+h*ky1/2)
    kx3 = xrate(ix+h*kx2/2,iy+ky2*h/2)
    ky3 = yrate(ix+h*kx2/2,iy+ky2*h/2)
    kx4 = xrate(ix+h*kx3,iy+ky3*h)
    ky4 = yrate(ix+h*kx3,iy+ky3*h)
    u1 = (kx1+2*kx2+2*kx3+kx4)/6
    ky4 = yrate(ix+h*ky3,iy+h)
    v1 = (ky1+2*ky2+2*ky3+ky4)/6
    #step = 0.0001 
    ix = (ix + u1*h)
    iy = (iy + v1*h)
    list1.append(ix)
    list2.append(iy) 
    global nh
    global switch
    nh +=1
    if ix >= 18 and iy >=15 and switch == 0:
        ft = nh
        switch = 1
        print('Time taken is to first attain the required density is',ft*h,'years')
    return

'''def trajectory_disc(ixd,iyd):
    u2 = xrate(ixd,iyd)
    v2 = yrate(ixd,iyd)
    #xstep = 0.001 
    #ystep = 0.001 
    ixd = ixd + u2*xstep
    iyd = iyd + v2*ystep
    list3.append(ixd)
    list4.append(iyd)
    return '''

list1 = [inx,]
list2 =[iny,]
list3 = [inx,]
list4 =[iny,]

trajectory(inx,iny)
'''trajectory_disc(inx,iny)'''

n=0
while (list1[-1]>1 and list2[-1]>1 and n<1000000):
    trajectory(list1[-1],list2[-1])
    n+=1

n = 0
'''while (list3[-1]>1 and list4[-1]>1 and n<1000000):
    trajectory_disc(list3[-1],list4[-1])
    n+=1
'''
#Plotting
fig = plt.figure()
plt.plot(list1,list2)
lx = np.linspace(-1,lim)
plt.plot(lx,len(lx)*[r1/a], color = 'r', label= 'Prey isocline')
ly = np.linspace(-1,lim)
plt.plot(list([d2/g/a])*len(ly), ly,color = 'g', label= 'Predator isocline')

plt.plot(lx,len(lx)*[15],color = '#01A42199', linestyle ='--',label= 'Target Pred')
plt.plot(list([18])*len(ly),ly,color = '#A4210199', linestyle ='--',label= 'Target Prey')
plt.scatter(18,15,label= 'Minimum target')

plt.quiver(x,y,u,v)
plt.xlim(-1,lim)
plt.ylim(-1,lim)
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.title('Continuous')
plt.legend()
fig.savefig('asnmt-predprey-cont.png')
fig.show()
#--------
'''
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

fig2.savefig('alv-predprey-disc.png') 
'''
plt.show()
#fin
