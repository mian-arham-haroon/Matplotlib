import matplotlib.pyplot as plt
import numpy as np

x=["python","C++","C","java"]
y=[85,70,60,82]
z=[35,40,20,42]
# p=[0,1,2,3]
p=np.arange(len(x))
width=0.4
p1=[j+width for j in p]
plt.title("Current famous",fontsize=10)
plt.xlabel("language")
plt.ylabel("no")
# c=["r","g","b","y"]
# plt.bar(x,y,width=0.3,color="y",align="center",edgecolor="r",linewidth=10,linestyle=":",alpha=0.4,
#         label="arham",)
plt.barh(x,y,color="y",label="arham")
plt.barh(x,z,color="r",label="12arham")
# plt.bar(p,y,width,color="y",label="arham")
# plt.bar(p1,z,width,color="r",label="12arham")
# plt.xticks(p+width/2,x)
plt.legend()

plt.show()












