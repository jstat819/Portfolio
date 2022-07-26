import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title = 'My Webpage', page_icon = ':tada:', layout = 'wide')

def loadlurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

coding_anim = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_v4isjbj5.json')

with st.container():
    st.subheader('Hi I go by Klepto :wave:')
    st.title('An aspiring software engineer from the UK')
    st.write('At the moment I am only knowledgeable of python, but I am branching out into HTML, CSS and JavaScript')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('My Experience')
        st.write('##')
        st.write('Making random stuff in python :smile:')
    with right_column:
      st_lottie(coding_anim, height = 300, key = 'coding')
