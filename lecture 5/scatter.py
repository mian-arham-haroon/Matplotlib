import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[21,12,43,94,37,96]
c=['r','g','y','b','g','r']
size=[10,2,4,9,6,3]
plt.scatter(x,y,color=c,s=size,alpha=0.7)
plt.title('Scatter Plot',fontsize=20)
plt.xlabel("day",fontsize=20)
plt.xlabel("no.",fontsize=20)
plt.show()

