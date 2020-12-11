from mpl_toolkits import mplot3d
import matplotlib.pyplot as fig
import numpy as ny 


ax=fig.axes(projection='3d')

x=ny.linspace(-20,20,50)
y=ny.linspace(-20,20,50)

X, Y = ny.meshgrid(x,y)

Z=ny.sin(ny.sqrt(x ** 2 + Y ** 2))

ax.contour3D(X,Y,Z, 50,cmap='Greys')

ax.set_xlabel('eixo x')
ax.set_ylabel('eixo y')
ax.set_zlabel('eixo z')
