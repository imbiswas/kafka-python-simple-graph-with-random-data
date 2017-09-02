import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

def animate(i):
    graph_data=open('doc.csv','r').read()
    lines=graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>0:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)
    ax.clear()
    ax.plot(ys,xs)

ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()


