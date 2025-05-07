import matplotlib.pyplot as plt


x=[10,20,30,40,50,60,70,120]

# plt.boxplot(x,notch=False,whis=2,vert=True,widths=0.09,tick_labels=['arham'],patch_artist=True,showmeans=True)
plt.boxplot(x,notch=False,sym='y+',vert=True,widths=0.09,tick_labels=['arham'],patch_artist=True,showmeans=True)

plt.show()