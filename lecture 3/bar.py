import matplotlib.pyplot as plt
import numpy as np

x=["arham","ali","aleena"]
y=[99,88,33]
z=[25,68,13]
width=0.1
p=np.arange(len(x))
p1=[j+width for j in p]
plt.xlabel("name",fontsize=10)
plt.ylabel("marks")
plt.title("students")
# plt.bar(x,y,width=0.3 ,colore="yellow")
# c=["y","b","m"]
# plt.bar(x,y,width=0.3,color=c,edgecolor="r",linewidth=10,linestyle=':',alpha=0.5)
plt.bar(p,y,width,color="r",label="arham")
plt.bar(p1,z,width,color="g",label="arham")
plt.legend()
plt.show()
print(p)




