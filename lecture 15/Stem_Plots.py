import matplotlib.pyplot as plt


x=[1,2,3,4,5,6]
y=[2,4,8,9,6,4]

plt.stem(x,y,linefmt=":",markerfmt="ro",basefmt="g",label="arham",bottom=6,orientation='horizontal')                                                   #  ,use_line_collection=False
plt.legend()
plt.show()