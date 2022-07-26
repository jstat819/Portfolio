import streamlit as st

st.set_page_config(page_title = 'My Portfolio', page_icon = ':tada:', layout = 'wide')

with st.container():
  st.subheader('Hi, I go by Klepto :wave:')
  st.title('I am an aspiring software engineer from the UK')
  st.write('At the moment the only programming language I know is python, but I am soon going to learn HTML, CSS and JS, as well as C#')

with st.container():
  st.write('---')
  left_column, right_column = st.columns(2)
  with left_column:
    st.header('What I do')
    st.write('Create terrible programs on replit.com :smile:')
