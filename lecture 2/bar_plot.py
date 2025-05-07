import matplotlib.pyplot as plt

x=["arham","ali","aleena"]
y=[99,88,33]
plt.xlabel("name",fontsize=10)
plt.ylabel("marks")
plt.title("students")
# plt.bar(x,y,width=0.3 ,colore="yellow")
c=["y","b","m"]
plt.bar(x,y,width=0.3,color=c)
plt.show()




