import matplotlib.pyplot as plt

x=["python","C++","C","java"]
y=[85,70,60,82]
plt.title("Current famous",fontsize=10)
plt.xlabel("language")
plt.ylabel("no")
c=["r","g","b","y"]
plt.bar(x,y,width=0.3,color=c,align="center",edgecolor="r",linewidth=10)
plt.show()












