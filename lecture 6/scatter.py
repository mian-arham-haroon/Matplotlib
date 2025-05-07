import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[21,12,43,94,37,96]
z=[3,4,9,7,2,5]
# c=['r','g','y','b','g','r'] 
color=[10,29,27,33,11,21] 
size=[101,211,411,239,516,322]
# plt.scatter(x,y,color=c,s=size,alpha=0.7,marker='*',edgecolors='g',linewidths=2) 
plt.scatter(x,y,c=color,s=size,alpha=0.7,cmap="BrBG") 
plt.scatter(x,z,c="r",s=size,alpha=0.7) 
t=plt.colorbar()
t.set_label("arham",fontsize=20)
plt.title('Scatter Plot',fontsize=20)
plt.xlabel("day",fontsize=20)
plt.xlabel("no.",fontsize=20)
plt.show()

