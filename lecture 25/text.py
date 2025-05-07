import matplotlib.pyplot as plt


x=[1,2,3,4,5,6]
y=[3,4,2,5,4,2]


plt.plot(x,y)
plt.title("arham",fontsize=10)
plt.xlabel("x",fontsize=10)
plt.ylabel("y",fontsize=10)
# plt.text(3,4,"arham",fontsize=10,style="italic",bbox={"facecolor":"red"})
# plt.annotate("python",xy=(3,2),xytext=(4,4),arrowprops=dict(facecolor="black",shrink=100))
plt.legend(["line"],loc=1,facecolor="yellow",framealpha=0.4,edgecolor="k",shadow=True)






plt.show()