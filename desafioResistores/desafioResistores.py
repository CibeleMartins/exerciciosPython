import streamlit as st

with st.container():

    st.header("Desafio de resistores!")
    st.text("Receba o valor de uma resistencia e a traduza para suas respectivas cores.")

    st.text_input(label="Digite o valor da resistencia",value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
