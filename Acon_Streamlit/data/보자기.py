# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 06:29:35 2022

@author: PedoSiki
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
#%matplotlib inline
ae = pd.read_csv("인구밀도1820.csv",encoding='cp949',sep=',' ,header=[0],index_col=[0])

fig, ax = plt.subplots()
rc('font', family='Malgun Gothic')
x = np.arange(len(ae.index))
wd = 0.25

ax.bar(x, ae['2018'], color = 'green', width=wd )
ax.bar(x+wd, ae['2019'], color = 'skyblue', width=wd )
ax.bar(x+2*wd, ae['2020'], color = 'orange', width=wd)

ax.set_xticks(x+wd )
ax.set_xticklabels(ae.index )
ax.set_yticks(np.arange(0,16001,500))

ax.set_title("지역별 인구밀도")
ax.set_xlabel('지역')
ax.set_ylabel("인구밀도")

ax.legend(ae.columns)

#st.pyplot(fig)