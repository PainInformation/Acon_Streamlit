import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


def app():
    st.subheader("지역별 인구밀도")
    st.write("출처:통계청")
    ae = pd.read_csv("./data/인구밀도1820.csv",encoding='cp949',sep=',' ,header=[0],index_col=[0])
    st.table(ae)

    st.subheader("matplotlib 차트로 표현")
    fig, ax = plt.subplots(figsize=(30,20))
    
    rc('font', family='Malgun Gothic')
    x = np.arange(len(ae.index))
    wd = 0.25

    ax.bar(x, ae['2018'], color = 'green', width=wd )
    ax.bar(x+wd, ae['2019'], color = 'skyblue', width=wd )
    ax.bar(x+2*wd, ae['2020'], color = 'orange', width=wd)

    ax.set_xticks(x+wd )
    ax.set_xticklabels(ae.index ,size=12)
    ax.set_yticks(np.arange(0,16001,250))

    ax.set_title("지역별 인구밀도(명/km^2)" , size=20)
    ax.set_xlabel('지역' , size=14)
    ax.set_ylabel("인구밀도", size=14)

    ax.legend(ae.columns)
    st.pyplot(fig)
    
    st.subheader("streamlit 기본차트로 표현")
    st.bar_chart(ae,  use_container_width=True)
