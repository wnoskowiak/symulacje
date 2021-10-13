import numpy as np
import matplotlib.pyplot as plt
import get_brown

brownian_motions=get_brown.get_brownian_motion(5000,10)
trajectories=np.cumsum(brownian_motions,axis=0).transpose()

opis = []
for i in range(10):
    plt.plot(trajectories[i], linewidth=1, alpha=0.7)
    opis.append('Cząstka: {}'.format(i))


plt.axhline(0,color='black')
plt.xlabel("krok")
plt.ylabel("odchylenie od położenia początkowego")
plt.legend(opis)
plt.show()