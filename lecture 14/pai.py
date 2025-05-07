import matplotlib.pyplot as plt


x=[10,20,30,40]
y=['c','c++','java','python']
ex=[0.2,0.0,0.0,0.0]
c=['r','y','g','b']
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.1f%%",shadow=True,radius=1.2,labeldistance=1.1,startangle=90
,textprops={"fontsize":15},counterclock=False,wedgeprops={"linewidth":1})
plt.show()    

































