import numpy as np 
import matplotlib.pyplot as plt

h=0.1
alpha=1
x0=0.5
y=int(7/h)

def f(x):
    return -alpha*x

x=np.zeros(y+1)
t=np.linspace(0, 7, y+1)

x[0]=x0


for i in range(y):
    x[i+1]=x[i]+h*f(x[i])
    
   
   
a = np.linspace(0, 7, 256) 
b=np.exp(-alpha*a)*x0
    
plt.plot(t, x, label='Numerisch') 
plt.plot(a, b, label='Exakt')
plt.legend(loc='upper right')
plt.axis([0, 7, 0, 0.6])
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('A.3 a)')
plt.show()

