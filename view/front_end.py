import streamlit as st
import controller.cnf_conversion.after_conversion as grammar
import controller.cyk_algorithm.execution as cyk

def start_fe():
  st.set_page_config(page_title='CYK Algorithm', page_icon='::tada::', layout='wide')
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