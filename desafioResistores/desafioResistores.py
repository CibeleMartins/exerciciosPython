import streamlit as st


from colorama import init
from termcolor import colored

import IEC60062 as mostrar_cores

st.set_page_config(page_title="Cores resistores!", layout='centered')

with st.container():

    # with open('style.css') as style:

    #     st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)

    st.header("Desafio de resistores!")
    st.text("Receba o valor de uma resistencia e a traduza para suas respectivas cores.")

    valor_resistencia = st.text_input(label="Digite o valor da resistencia",value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")

    button = st.button(label="Ver cores")


dict_cores = {
        'Preto': 'black',
        # 'Marrom': fg('brown'),
        'Vermelho': 'red',
        # 'Laranja': fg('orange'),
        'Amarelo': 'yellow',
        'Verde': 'green',
        'Azul': 'blue',
        'Violeta': 'violet',
        # 'Cinza': fg('grey'),
        'Branco': 'white'
}


if button and len(valor_resistencia) > 0:

    mostrar_cores.IEC60062(valor_resistencia)

    lista_cores = mostrar_cores.IEC60062(valor_resistencia).copy()

    for i in lista_cores:

        cor_dict_cores = dict_cores[i]

        init()
        st.(colored(i, cor_dict_cores, 'on_red'))         

    









