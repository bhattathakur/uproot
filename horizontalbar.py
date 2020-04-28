"""
====================
Horizontal bar chart
====================

This example showcases a simple horizontal bar chart.
"""
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
#np.random.seed(19680801)
x=[]
y=[]
filename="allpdg.dat"
savefile="pdgall.png"
with open(filename) as f:
    for line in f:
        words=line.strip().split("\t")
        x.append(words[0])
        y.append(int(words[1]))
#plt.rcdefaults()
fig, ax = plt.subplots()
print("x-list\n",x)
print("y-list\n",y)

# Example data
#people = ('tom', 'dick', 'harry', 'Slim', 'Jim')
#y_pos = np.arange(len(people))
#performance = 3 + 10 * np.random.rand(len(people))
#error = np.random.rand(len(people))

ax.barh(x, y,align='center')
#ax.set_yticks(y)
#ax.set_yticklabels(y)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('count')
ax.set_ylabel('Particle id (pdg) for isotopes')
ax.set_title('')
plt.tick_params(axis='y',which='major',labelsize=8.0) #added to manage the size of text
plt.xscale("log")
plt.yticks(rotation=15)
fig.savefig(savefile,format='png',dpi=200)
plt.show()
