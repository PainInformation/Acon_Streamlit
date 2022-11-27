import streamlit as st
from multiapp import MultiApp
from pro2 import one, two
from pro2 import three

def app():    
    st.title("과제2")    
    app = MultiApp()
    app.add_app("자료개요" , one.app)
    app.add_app("테이블" , two.app)
    app.add_app("차트" , three.app)   
    app.rd_run()
   


