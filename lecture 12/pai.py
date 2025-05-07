import matplotlib.pyplot as plt


x=[10,20,30,40]
y=['c','c++','java','python']
ex=[0.2,0.0,0.0,0.0]
c=['r','y','g','b']
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.1f%%")
plt.show()    

































