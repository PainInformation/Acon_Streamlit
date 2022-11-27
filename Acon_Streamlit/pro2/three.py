import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def app():
        
        rc('font', family='NanumBarunGothic')
        ph = './data/tem_mk/'
        
        st.subheader("2022-06-21~27일 매일 평균")
        a= pd.read_csv(ph+"OBS_108_AirTemp_diurnal_data",encoding='cp949',sep=',' ,index_col=[0])
        n=pd.to_datetime(a.index)

        fig, ax = plt.subplots()
        ax.set_xlabel('2022/06')
        ax.set_xticklabels(n.day)
        ax.set_ylim(-20,40)
        ax.plot(a['mean'])
        st.pyplot(fig)

        st.subheader("2022-06-21~27일 시간당 평균")
        b = pd.read_csv(ph+"OBS_108_AirTemp_hourly_data",encoding='cp949',sep=',' ,index_col=[0])
        n=pd.to_datetime(b.index)
     
        fig, ax = plt.subplots(figsize=(30,20))
        ax.set_xlabel('2022/06')
        ax.set_xticklabels(n.strftime('%d.%H'), size=7)
        ax.xaxis.set_tick_params(rotation=60) 
        ax.set_ylim(-20,40)
        line=ax.plot(b['mean'])
        st.pyplot(fig)
        #st.line_chart(line)

        
        st.subheader("2021-06-26 ~ 2022-06-27 매달 평균")
        c = pd.read_csv(ph+"OBS_108_AirTemp_month_data",encoding='cp949',sep=',' ,index_col=[0])
        n=pd.to_datetime(c.index)

        fig, ax = plt.subplots()        
        ax.set_xticklabels(n.date , size=10)
        ax.xaxis.set_tick_params(rotation=20) 
        ax.set_ylim(-20,40)
        ax.plot(c['mean'])
        st.pyplot(fig)

        st.subheader("2021-06-26 ~ 2022-06-27 매일 평균")
        d = pd.read_csv(ph+"OBS_108_AirTemp_2021_data",encoding='cp949',sep=',' ,index_col=[0])
        st.line_chart(d['mean'])
