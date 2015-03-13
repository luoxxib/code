#-*- coding: utf-8 -*-
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=18) 
rcParams["savefig.dpi"] = 600

    
df = pd.read_csv("h:/ndy.csv")
flights = df.pivot("year","month","ndvi")
flights = flights.reindex(columns=df.iloc[:12].month)

fig = plt.figure(figsize=(9,7))
ax1 = fig.add_subplot(111)

cmap = sns.light_palette('green', n_colors=8, reverse=False, as_cmap=True)
aa = sns.heatmap(flights, annot=True, fmt="0.2g",ax=ax1,linewidths=.01,cmap=cmap)

#aa.set_xticklabels(rotation=45, horizontalalignment='right')
plt.xlabel(u'月份',fontproperties=font)
plt.ylabel(u'年份',fontproperties=font)

axis = aa.xaxis
labels = axis.get_ticklabels()
for label in labels:
    label.set_rotation(25)
    label.set_horizontalalignment('right')
    
axis = aa.yaxis
labels = axis.get_ticklabels()
for label in labels:
    label.set_rotation(0)
    #label.set_horizontalalignment('center')

#plt.savefig('h:/tt.jpg',dpi=600)
plt.show()
