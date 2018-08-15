import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = []
Y = []
Z = []

fig = plt.figure()
ax = Axes3D(fig)

RT = 80/3. #replace 80 with 40 for the SJF
TT = 140/3. #replace 140 with 100 for SJF

for i in xrange(101):
    for j in xrange(101):
        X.append(i)
        Y.append(j)
        Z.append((RT**2)*i + j*TT)

ax.scatter(X,Y,Z)
plt.show()

