import streamlit as st
import controller.cnf_conversion.after_conversion as grammar
import controller.cyk_algorithm.execution as cyk
import controller.cnf_conversion.cfg as cfg


def start_fe():
  title = 'Parsing Sintaksis Kalimat Bahasa Indonesia Menggunakan Algoritma CYK'
  st.set_page_config(page_title='CYK Algorithm', page_icon='::tada::', layout='wide', menu_items={
    'About': f"""
      ### {title}
      Made with :heart: oleh kelompok 3 kelas E 
      Teori Bahasa dan Otomata
      GitHub: https://github.com/gedeapriana/indonesian-sentence-cyk
      """
  })

  st.write("<h2 style='text-align: center;'>Aplikasi Pengecekan Kalimat Bahasa Indonesia</h2>", unsafe_allow_html=True)
  st.write("<h5 style='text-align: center;'> GitHub: <a href='https://github.com/gedeapriana/indonesian-sentence-cyk'>gedeapriana/indonesian-sentence-cyk</a></h2>", unsafe_allow_html=True)
  st.write('')

  final_dic = grammar.get_grammar()

  cfg.display(final_dic)

  write_cfg = open("controller/cnf_conversion/cnf-all.txt", "w")
  write_cfg.writelines(set(final_dic))

  with st.container():
    st.write('---')
    input_column, rule_column = st.columns(2)
    with input_column:
      string_input = st.text_input(' ', placeholder='Masukkan kalimat Bahasa Indonesia')
      check_button = st.button('Cek', type='primary')
      if check_button:

        if len(string_input) == 0:
          st.error('Form tidak boleh kosong!')
        else:
          cyk.cyk_parse(final_dic, string_input)


    with rule_column:
      st.write('### CNF Rules:')
      st.write(final_dic)
