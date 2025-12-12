import matplotlib.pyplot as plt
import matplotlib.animation as animation
from psutil import cpu_percent

cpu_perc=[]

#for how many sec we need to keep CPU % window
frame_length=200
def animate(i):
    cpu_perc.append(cpu_percent())

    if(len(cpu_perc) <= frame_length):
       plt.cla() #clear
       if(len(cpu_perc)>=20):
           plt.plot(cpu_perc,'b',label="CPU Usage")
       else:
           plt.plot(cpu_perc,'g',label="CPU Usage")
    print(cpu_perc)
    plt.ylim(0,100)
    plt.xlabel("Time")
    plt.ylabel("CPU uses(%)")
    plt.legend(loc="upper right")

    #Matplotlib's tight_layout is a function that automatically adjusts subplot parameters to give specified padding.
    #It's a handy tool to remove unnecessary white space from your plots, making your visualizations cleaner and easier to interpret.
    plt.tight_layout()

#1000 milisec
ani = animation.FuncAnimation(plt.gcf(),animate,interval=1000)
plt.show()
