import streamlit as st
import pandas as pd

empty = '\u2205'
get_rhs = []  # menampung semua rhs dari cnf

def cyk_parse(cnf, string):

  n = len(string.split())
  table_filling = [[set([]) for j in range(n)] for i in range(n + 1)]

  # FIRST STEP
  get_all_rhs(cnf, n)
  flag = string_exist(string, n)

  # SECOND STEP
  is_acc = ''
  print(is_acc)

  # THIRD STEP
  filling_bottom(cnf, string, table_filling, n)
  filling_all(cnf, string, table_filling, n)
  is_accepted(table_filling, cnf, flag, n)

# ------------- SUB FUNCTIONS -----------------

def get_all_rhs(cnf, n):
  for i in range(0, n):
    for lhs, rule in cnf.items():
      for rhs in rule:
        get_rhs.append(rhs)

def string_exist(string, n):
  for i in range(0, n):
    if string.split()[i] not in get_rhs:
      return -1
  return 1

def filling_bottom(cnf, string, table_filling, n):
  string_split = string.split()
  for i in range(0, n):
    for lhs, rule in cnf.items():
      for rhs in rule:
        if len(rhs.split()) == 1 and rhs == string_split[i]:
          table_filling[i][i].add(lhs)

def filling_all(cnf, string, table_filling, n):
  with st.expander('Lihat Filling Table'):
    for i in range(0, n):
      for j in range(i, -1, -1):
        for k in range(j, i + 1):
          for lhs, rule in cnf.items():
            for rhs in rule:
              if len(rhs.split()) == 2 and rhs.split()[0] in table_filling[j][k] and rhs.split()[1] in table_filling[k + 1][i]:
                table_filling[j][i].add(lhs)
      st.table(pd.DataFrame(table_filling, columns=string.split()))
    print(pd.DataFrame(table_filling))

def is_accepted(table_filling, cnf, flag, n):
  if list(cnf.keys())[0] in table_filling[0][n-1] and flag == 1:
    is_acc = st.success('Kalimat diterima dalam tata Bahasa Indonesia')
    print('Kalimat diterima dalam tata Bahasa Indonesia')
    st.balloons()
  elif flag == -1:
    is_acc = st.warning('Kata dalam kalimat tidak terdapat pada rule')
    print('Kata dalam kalimat tidak terdapat pada rule')
  else:
    is_acc = st.error('Kalimat tidak valid')
    print('Kalimat tidak valid')
  return is_acc