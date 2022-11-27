import streamlit as st
import pandas as pd
import numpy as np


def app():
        ph = './data/tem_mk/'
        
        st.subheader("2022-06-21~27일 매일 평균")        
        a= pd.read_csv(ph+"OBS_108_AirTemp_diurnal_data",encoding='cp949',sep=',' ,index_col=[0])
        st.dataframe(a)

        st.subheader("2022-06-21~27일 시간당 평균")
        b = pd.read_csv(ph+"OBS_108_AirTemp_hourly_data",encoding='cp949',sep=',' ,index_col=[0])
        st.dataframe(b)

        st.subheader("2021-06-26 ~ 2022-06-27 매달 평균")
        c = pd.read_csv(ph+"OBS_108_AirTemp_month_data",encoding='cp949',sep=',' ,index_col=[0])
        st.dataframe(c)

        st.subheader("2021-06-26 ~ 2022-06-27 매일 평균")
        d = pd.read_csv(ph+"OBS_108_AirTemp_2021_data",encoding='cp949',sep=',' ,index_col=[0])
        st.dataframe(d)
