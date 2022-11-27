import streamlit as st

def app():       
        st.markdown("### 가상환경구축")
        st.markdown("- 가상환경 설치\n"
                    "   - conda create -n 이름 python=3.7.4 ipython numpy matplotlib pandas scipy scikit-learn tensorflow keras.1\n")
                   
        st.markdown("- 필요 라이브러리 설치\n"
                    "   1. pip install streamlit.1\n"
                    "   2. pip install seaborn\n"
                    "   3. pip install pandas_datareader\n"
                    "   4. pip install streamlit_folium\n"
                    "   5. pip install imageio-ffmpeg\n" )
        st.markdown("- 활성화\n"
                         
                    "   - conda activate 이름\n")
        st.markdown("- streamlit 실행\n"
                         
                    "   - streamlit run 실행.py \n")
                
