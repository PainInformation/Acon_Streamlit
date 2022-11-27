import streamlit as st
from multiapp import MultiApp
from mypage import project1 ,project2 ,home

app = MultiApp()

app.add_app("Home" , home.app)
app.add_app("과제1번" , project1.app)
app.add_app("과제2번" , project2.app)
app.sel_run()
