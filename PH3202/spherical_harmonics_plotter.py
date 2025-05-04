#!/Users/rajesh/py3cbc/bin/python
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm
from matplotlib.colors import LightSource

# Define the parameters for spherical harmonics
l = 2  # degree
m = 0  # order
Np=40
# Create a grid of theta and phi values
theta = np.linspace(0, np.pi, Np)
phi = np.linspace(0, 2 * np.pi, Np)
theta, phi = np.meshgrid(theta, phi)

# Compute the spherical harmonics Y(l, m)
Y_lm = sph_harm(m, l, phi, theta)

# Convert spherical coordinates to Cartesian coordinates for 3D plotting
x1 = np.abs(np.real(Y_lm)) * np.sin(theta) * np.cos(phi)
y1 = np.abs(np.real(Y_lm)) * np.sin(theta) * np.sin(phi)
z1 = np.abs(np.real(Y_lm)) * np.cos(theta)
x2 = np.abs(np.imag(Y_lm)) * np.sin(theta) * np.cos(phi)
y2 = np.abs(np.imag(Y_lm)) * np.sin(theta) * np.sin(phi)
z2 = np.abs(np.imag(Y_lm)) * np.cos(theta)
ls1 = LightSource(250, 45)
ls2 = LightSource(250, 45)
rgb1 = ls1.shade(np.real(Y_lm), cmap=cm.jet, vert_exag=0.1)
rgb2 = ls2.shade(np.imag(Y_lm), cmap=cm.jet, vert_exag=0.1)
# Create a 3D plot
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax2 = fig.add_subplot(1,2,2, projection='3d')
ax1.set_position([0,0,0.6,1])
ax1.plot_surface(x1, y1, z1,rstride=1, cstride=1, facecolors=rgb1, linewidth=0, antialiased=False, shade=False)

ax1.plot_wireframe(x1,y1,z1, color='w', alpha=0.1)
ax1.set_title(f'Re Y({l},{m})', y=0.9, size=18)

ax2.set_position([0.5,0,0.6,1])
ax2.plot_surface(x2, y2, z2,rstride=1, cstride=1, facecolors=rgb2, linewidth=0, antialiased=False, shade=False)
ax2.plot_wireframe(x2,y2,z2, color='w', alpha=0.1)
ax2.set_title(f'Im Y({l},{m})',y=0.9, size=18)

ax1.axis('off')
ax2.axis('off')
plt.show()