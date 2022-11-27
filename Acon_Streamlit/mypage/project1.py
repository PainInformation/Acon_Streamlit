import streamlit as st
from multiapp import MultiApp
from pro1 import wagu , 그랭프 , start


def app():
    st.title("과제1")
    app = MultiApp()
    app.add_app("설치명령어" , start.app)
    app.add_app("스트리밋 기능 일부" , wagu.app)
    app.add_app("그래프" , 그랭프.app)
    app.rd_run()
