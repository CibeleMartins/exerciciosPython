import streamlit as st

import IEC60062 as mostrar_cores

st.set_page_config(page_title="Cores resistores!", layout='centered')

with st.container():

    st.header("Desafio de resistores!")
    st.text("Receba o valor de uma resistencia e a traduza para suas respectivas cores.")

    valor_resistencia = st.text_input(label="Digite o valor da resistencia", value="", max_chars=None, key=None, type="default", help=None,
                                      autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")

    button = st.button(label="Ver cores")

dict_cores = {
    'Preto': '#000000',
    'Marrom': '#8B4513',
    'Vermelho': '#FF0000',
    'Laranja': '#FFA500',
    'Amarelo': '#FFFF00',
    'Verde': '#008000',
    'Azul': '	#0000FF',
    'Violeta': '#A020F0',
    'Cinza': '#808080',
    'Branco': '#FFFFFF',
    'Rosa': '#FF1493',
    'Prata': '#C0C0C0',
    'Dourado': '#FFD700'
}

if button and len(valor_resistencia) > 0:

    mostrar_cores.IEC60062(valor_resistencia)

    lista_cores = mostrar_cores.IEC60062(valor_resistencia).copy()
    count = 0

    for i in lista_cores:

        count += 1
        st.color_picker(i, dict_cores[i], key=count)
