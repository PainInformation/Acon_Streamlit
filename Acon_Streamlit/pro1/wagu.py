import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.datasets import load_iris

def app():
    ## Title
    st.title('일부기능들')

    ## Header/Subheader
    st.header('This is header')
    st.subheader('This is subheader')

    ## Text
    st.text("Hello Streamlit! ")


   
    ## data
    iris = load_iris()
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df['target'] = iris['target']
    iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))

    ## Return table/dataframe
    # table
    st.table(iris_df.head())

    # dataframe
    st.dataframe(iris_df)
    st.write(iris_df)


    st.write("위젯?")
    ## Checkbox
    if st.checkbox("Show/Hide"):
        st.write("체크박스 선택")
    ## button
    st.button("About")
    ## Radio button
    status = st.radio("Select status.", ("Active", "Inactive"))
    if status == "Active":
        st.success("라디오 박스 활성화")
    else:
        st.warning("라디오 박스 비활성화")


    ## Select Box
    occupation = st.selectbox("선택값 ",
                              ["1","2","3"])
    st.write("선택 값 ", occupation)



    ## Sidebars
    # st.echo, st.spinner, st.write 안됨  
    st.sidebar.header("임시")
    st.sidebar.selectbox("작동안함.", ["1번", "2번", "3번"])



    ## line chart
    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['피자', '치킨', '파스타'])

    st.line_chart(chart_data)

    ## map
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.50, 127.00],
        columns=['lat', 'lon'])

    st.map(map_data)

    ## progress
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
      latest_iteration.text(f'임시 진행프로세스 {i+1}%')
      bar.progress(i + 1)
      time.sleep(0.05)

