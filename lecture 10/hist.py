import matplotlib.pyplot as plt
import numpy as np
import random


x=np.random.randint(10,60,(50))

no=[23, 59, 52, 20, 43, 54, 13, 55, 43, 11, 50, 18, 59, 19, 58 ,24, 49, 35, 19, 59, 38, 10, 34, 35,
    49, 15, 49, 21, 40, 14, 53, 18, 44, 31, 48, 52, 34, 23, 23, 34, 34, 40, 15, 24, 55, 33, 40, 42,
    59, 54]
l=[10,20,30,40,50,60]
# plt.hist(no,"auto",(0,200),color="y",edgecolor="r",bins=l)
# plt.hist(no,"auto",(0,100),color="y",edgecolor="r")
# plt.hist(no,color="y",edgecolor="r",cumulative=-1)
# plt.hist(no,color="y",edgecolor="r",bottom=10,align='left') 
# plt.hist(no,color="y",edgecolor="r",bottom=10,histtype='step') 
# plt.hist(no,color="y",edgecolor="r",bottom=10,orientation='horizontal') 
# plt.hist(no,color="y",edgecolor="r",bottom=10,rwidth=0.6,log=True) 
plt.hist(no,color="y",edgecolor="r",bottom=10,rwidth=0.6,label="arham")
plt.axvline(40,color='g',label='line')
plt.legend() 
plt.title("Student")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.grid()
plt.show()








