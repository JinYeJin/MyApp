import streamlit as st
import pandas as pd


st.write("""
안녕하세요
""")

url = st.text_input(label='Enter some text')
form = st.form("my_form")
form.form_submit_button("Submit")
print(url)
