import streamlit as st

import funcao.IEC60062 as mostrar_cores

with st.container():

    with open('style.css') as style:

        st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)

    st.header("Desafio de resistores!")
    st.text("Receba o valor de uma resistencia e a traduza para suas respectivas cores.")

    valor_resistencia = st.text_input(label="Digite o valor da resistencia",value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")

    button = st.button(label="Ver cores")

if button:

    mostrar_cores.IEC60062(valor_resistencia)
