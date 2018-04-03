import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("laminas.txt")
enAlbum=data[:, 0]
repetidas=data[:, 1]

sobres=range(len(enAlbum))

plt.plot(sobres, enAlbum,'ro', label="Laminas en el album")
plt.scatter(sobres, repetidas, label="repetidas")
plt.xlim(-5, 180)
plt.legend()
plt.show()
#plt.savefig("graficaAlbum.png")


