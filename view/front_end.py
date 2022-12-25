import requests
import streamlit as st
import controller.cnf_conversion.after_conversion as grammar
from streamlit_lottie import st_lottie
import controller.cyk_algorithm.execution as cyk

def start_fe():
  lottie = load_lottie_url("https://assets7.lottiefiles.com/temp/lf20_zLc23z.json")
  st.set_page_config(page_title='CYK Algorithm', page_icon='::tada::', layout='wide')
  st_lottie(lottie, height=300, key='coding')
  st.write("<h1 style='text-align: center;'>Aplikasi Pengecekan Kalimat Bahasa Indonesia</h1>", unsafe_allow_html=True)

  final_dic = grammar.get_grammar()
  with st.container():
    st.write('---')
    input_column, rule_column = st.columns(2)
    with input_column:
      string_input = st.text_input(' ', placeholder='Masukkan kalimat Bahasa Indonesia')
      check_button = st.button('Cek', type='primary')
      if check_button:

        if len(string_input) == 0:
          st.write('Form tidak boleh kosong!')
        else:
          cyk.cyk_parse(final_dic, string_input)


    with rule_column:
      st.write('### CNF Rules:')
      st.write(final_dic)

def load_lottie_url(url):
  req = requests.get(url)
  if req.status_code != 200:
    return None
  return req.json()