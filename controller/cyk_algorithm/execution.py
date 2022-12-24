import controller.cyk_algorithm.tringular_table as table
import copy
import streamlit as st

dic = {}

def exe(new_dic, filling_table, input_string):  # fungsi utama proses algoritma cyk
  count = 0  #inisiasi count = 0
  global dic  # jadikan variabel dic global
  dic = new_dic  # isikan variabel dic dengan hasil cnf yang sudah didapat
  str_table = copy.deepcopy(filling_table)
  print(str_table)
