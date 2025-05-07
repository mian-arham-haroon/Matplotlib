import matplotlib.pyplot as plt

x=[1,2,3,4,5]
area=[1,3,2,1,4]
area1=[2,4,5,2,1]
area2=[2,1,2,1,2]
l=["area","area1","area2"]
plt.stackplot(x,area,area1,area2,labels=l,colors=['k','g','y'],baseline='zero')
plt.title("ARHAM")
plt.xlabel("ASD")
plt.ylabel("123")
plt.grid()
plt.legend(loc=2)
plt.show()


