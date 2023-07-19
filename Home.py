import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')

st.header('The Best Company')
st.write("""At The Best Company, we believe in harnessing the collective 
         brilliance of our diverse team to create innovative solutions and drive 
         meaningful change. As a leading technology company, we are dedicated to 
         fostering an environment where our employees can thrive, learn, 
         and grow both personally and professionally.""")

st.subheader('Our Team')
col1, col2, col3 = st.columns(3)
df = pd.read_csv('data.csv', sep=',')

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(f"{row['role'].title()}")
        st.image('images/'+ row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(f"{row['role'].title()}")
        st.image('images/'+ row['image'])

with col3:
    for index, row in df[9:].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(f"{row['role'].title()}")
        st.image('images/'+ row['image'])


