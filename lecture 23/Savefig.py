import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[1,2,3,4,6,4]
plt.plot(x,y,color="r")


# plt.savefig("line1",dpi=2000,facecolor="k")
# plt.savefig("line2.pdf",dpi=2000,facecolor="k")
# plt.savefig("line3",transparent=True,dpi=2000,facecolor="k")
plt.savefig("line4",transparent=False,bbox_inches='tight',dpi=2000,facecolor="y")






















plt.show()