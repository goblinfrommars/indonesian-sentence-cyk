# table_schema = [['set' for _ in range(5)] for _ in range(5)]
#
# def gml(table):
#   max_leng = -1
#   for i in table:
#     temp = len(max(i, key=len))
#     print(temp + 5)
#
#
# gml(table_schema)
# for j in range(5):
#   i = 0
#   upper_bound = (j + 1) * 8 * '-' + (i + 2) * '-'
#   print(upper_bound)
#   print(' | ')
#
#   for k in range((5 - 1) - j, 5):
import copy

import controller.cnf_conversion.cnf as cnf
import controller.cyk_algorithm.create_filling_table as tab
# filling_table = [['' for _ in range(len(input_string.split(' ')))] for _ in range(len(input_string.split(' ')))]

input_string = 'baju itu disetrika oleh oleh'
dic = cnf.run_conversion()
get_rhs = []

def cyk_parse(string):
  n = len(string)
  table = [[set([]) for j in range(n)] for i in range(n + 1)]
  flag = 0

  for i in range(0, n):
    for lhs, rule in dic.items():
      for rhs in rule:
        get_rhs.append(rhs)

  for j in range(0, n):

    if string[j] not in get_rhs:
      flag = 1

    for lhs, rule in dic.items():
      for rhs in rule:
        if len(rhs.split()) == 1 and rhs == string[j]:
          table[j][j].add(lhs)

    for i in range(j, -1, -1):
      for k in range(i, j + 1):
        for lhs, rule in dic.items():
          for rhs in rule:
            if len(rhs.split()) == 2 and rhs.split()[0] in table[i][k] and rhs.split()[1] in table[k + 1][j]:
              table[i][j].add(lhs)

  for i in table:
    print(i)

  if list(dic.keys())[0] in table[0][n - 1]:
    print("Accepted")
  elif flag == 1:
    print('String not in grammar')
  else:
    print('Not Accepted')

cyk_parse(input_string.split())
