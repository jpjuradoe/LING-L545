#OSCILOGRAM
import parselmouth
#plotting libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#sns.set() #default style for graphs
sns.set_style("whitegrid")
#sns.set_palette("Greys", 8)
plt.rcParams['figure.dpi'] = 50 #large images

snd = parselmouth.Sound("1_r.wav") #to open a sound

plt.figure()
plt.plot(snd.xs(), snd.values.T)
plt.xlim([snd.xmin, snd.xmax])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.show() #or plt.savefig("sound.png"), or plt.savefig("sound.pdf")
