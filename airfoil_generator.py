import numpy as np
import matplotlib.pyplot as plt



naca = "4415"

m = int(naca[0]) / 100
p = int(naca[1]) / 10
T = int(naca[2:]) / 100

# x<p 
x1 = np.linspace(0,p,100)
yc1 = (m/p**2)*(2*p*x1 - (x1**2))
yt1 = 5*T*(0.2969*np.sqrt(x1) - 0.126*x1 - 0.3516*x1**2 + 0.2843*x1**3 - 0.1015*x1**4)
dx = x1[2] - x1[1]
dyc1_dx1 = np.gradient(yc1,dx)
k1 = np.arctan(dyc1_dx1)
X1 = x1 - np.sin(k1) * yt1
Y1 = yc1 + np.cos(k1) * yt1
X4 = x1 + np.sin(k1) * yt1
Y4 = yc1 - np.cos(k1) * yt1

# x>p 
x2 = np.linspace(p, 1, 100) 
yc2 = (m/(1-p)**2)*((1-2*p)+(2*p*x2) - (x2**2)) 
yt2 = 5*T*(0.2969*np.sqrt(x2) - 0.126*x2 - 0.3516*x2**2 + 0.2843*x2**3 - 0.1015*x2**4) 
dx2 = x2[2] - x2[1] 
dyc2_dx2 = np.gradient(yc2, dx2) 
k2 = np.arctan(dyc2_dx2) 
X2 = x2 + np.sin(k2) * yt2 
Y2 = yc2 - np.cos(k2) * yt2 

X3 = x2 - np.sin(k2) * yt2 
Y3 = yc2 + np.cos(k2) * yt2 


# plot 
plt.plot(x1, yc1, color = "blue",linestyle="--")
plt.plot(x2,yc2, color = "blue",linestyle="--")
plt.plot(X1,Y1,color="red",linestyle="-")
plt.plot(X2,Y2,color="red",linestyle="-")
plt.plot(X3,Y3,color="red",linestyle="-")
plt.plot(X4,Y4,color="red",linestyle="-")
plt.axis('equal')
plt.title(f"NACA {naca}")
plt.show()