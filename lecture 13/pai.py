import matplotlib.pyplot as plt


x=[10,20,30,40]
x1=[40,30,20,10]
y=['c','c++','java','python']
# ex=[0.2,0.0,0.0,0.0]
c=['r','y','g','b']
# plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.1f%%",shadow=True,radius=1.2,labeldistance=1.1,startangle=0,
# textprops={"fontsize":14},counterclock=False,wedgeprops={"linewidth":2,"edgecolor":"k"},center=(1,1),rotatelabels=False)

plt.pie(x,labels=y,radius=1.2)
# plt.pie(x1,radius=0.5)
# plt.pie([1],colors="w")
cr=plt.Circle(xy=(0,0),radius=0.7,facecolor="w")
plt.gca().add_artist(cr)              


# plt.title("arhmm")
# plt.legend(loc=4)
# plt.pie([1])             
plt.show()    

































