import streamlit as st

class MultiApp:
       def __init__(self) ->None:
              self.apps = []

       def add_app(self, title, func):
              self.apps.append({
                     "title": title,
                     "function": func
              })
              
       def rd_run(self):
              app = st.sidebar.radio(
                     '목록',
                     self.apps,
              format_func=lambda app: app['title'])
              app['function']()
              
       def sel_run(self):
              page = st.sidebar.selectbox(
                     '선택', 
                     self.apps, 
              format_func=lambda page: page['title'])
              page['function']()
