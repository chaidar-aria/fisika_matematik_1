# %% [markdown]
# # INTEGRASI NUMERIK PYTHON
#
# Metode Numerik untuk Integral yang dijelaskan pada Tutorial Python ini adalah
# 1. Metode Trapesium
# 2. Metode Simpson
# 3. Metode Gauss-Legendre 2 titik dan 3 titik

# %%
import pandas as pd
import matplotlib.pyplot as plt
from sympy import *
import numpy as np


# %%
x = symbols('x')

# %% [markdown]
# Contoh integral:
# $$ \int_{a}^{b}f(x)dx $$

# %%
# Definisi fungsi yang diintegralkan
f = x**3 - x

# %%
# Batas integral
a = 0
b = 2

# %%
# Ubah persamaan ke Sympy dengan fungsi python
ff = lambdify(x, f)

# %%
# buat data sebanyak n+1
# dari x = a ... b
n = 10
xd = np.linspace(a, b, n+1)
fd = ff(xd)
dx = xd[1]-xd[0]

# %%
# Buat pandas data frame untuk tampilan berbentuk tabel
data = {'x': xd, 'f(X)': fd}
df = pd.DataFrame(data)
df

# %% [markdown]
# ## METODE EKSAK

# %%
ieksak = integrate(f, (x, a, b))
ieksak


# %% [markdown]
# ## METODE TRAPESIUM

# %%
s = 0
for i in range(1, n):
    s += fd[i]
itrap = (dx/2)*(fd[0] + 2*s + fd[n])
itrap

# %%
# Galat relatif
errtrap = (itrap - ieksak)/ieksak
errtrap

# %% [markdown]
# ## METODE SIMPSON

# %%
s1 = 0
s2 = 0
for i in range(1, n, 2):
    s1 += fd[i]
for i in range(2, n-1, 2):
    s2 += fd[i]

isimp = (dx/3) * (fd[0] + 4*s1 + 2*s2 + fd[n])
isimp

# %%
# Galat relatif
errsimp = (isimp - ieksak)/ieksak
errsimp

# %% [markdown]
# ## METODE GAUSS LAGENDRE
#
# Langkah pertama adalah ubah bentuk integrak menjadi
#
# $$ \int_{a}^{b} f(x)dx = \frac{(b-a)}{2} \int_{-1}^{1}g(y)dy $$
#
# dengan
#
# $$ g(y) = f \left ( \frac{a+b}{2} + \frac{b-a}{2}y \right )$$
#
# Langkah kedua adalah gunakan bobot $ w_i $ dan posisi
#
# $$ \int_{-1}^{1} g(y)dy = \sum_{i=1}^{N} w_i g (y_i) $$
#
# Nilai posisi (Nodes) dan Bobot diberikan pada tabel berikut ini

# %%
y = symbols('y')

# %%
# Substitusi variabel x dengan (a+b).2 + (b-a)y/2

g = f.subs(x, (a+b)/2 + (b-1)*y/2)
g

# %%
# Ubah ke persamaan Sympy ke fungsi python
gg = lambdify(y, g)

# %%
w1 = 1.0
w2 = 1.0
x1 = -1/np.sqrt(3)
x2 = 1/np.sqrt(3)
igl2 = ((b-a)/2) * (w1*gg(x1) + w2*gg(x2))
igl2

# %%
errgl2 = (igl2 - ieksak)/ieksak
errgl2

# %%
# Menggunakan Gauss-Legendre 2 titik
w1 = 5/9
w2 = 8/9
w3 = 5/9
x1 = -np.sqrt(3/5)
x2 = 0
x3 = np.sqrt(3/5)
igl3 = ((b-a)/2) * (w1*gg(x1) + w2*gg(x2) + w3*gg(x3))
igl3

# %%
errgl3 = (igl3 - ieksak)/ieksak
errgl3
