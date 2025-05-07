import matplotlib.pyplot as plt # type: ignore

x=[1,2,3,4]
y=[3,1,4,2]

plt.plot(x,y)

# plt.xticks(x,labels=['c','y','s','a']) 
# plt.yticks(x)
plt.xlim(0,10)
plt.ylim(0,10)
plt.axis([0,10,0,7])

plt.show()