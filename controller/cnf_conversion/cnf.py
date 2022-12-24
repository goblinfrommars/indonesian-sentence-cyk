from controller.cnf_conversion.cfg import *

var_ls = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
new_rs = [] # menampung terminal baru setelah hasil konversi
new_ls = [] # menampung non terminal baru setelah hasil konversi


# jika lhs terdapat pada rhs, maka hapus lhs, tambahkan rhs dari lhs yang telah di hapus ke rhs
def first_step():
  key = list(dic.keys())  # simpan semua lhs dari dic, ke dalam bentuk list
  for i in key:  # melakukan perulangan pada key yang telah didapat
    for j in key:
      if i in dic[j]:  # jika lhs terdapat pada rhs
        dic[j].remove(i)  # hapus lhs
        dic[j].extend(dic[i])  # tambahkan rhs


# fungsi pertama yang dijakankan untuk proses penghapusan non terminal yang berjumlah  > 2
def second_step():
  while rule_max_length() > 2:  # selama masih terdapat lebih dari dua non terminal pada start state, lakukan perulangan
    for j in dic[start_symbol]:  # perulangan untuk mencari rhs dari start symbol
      if len(j.split(' ')) <= 2:  # jika rhs dari start symbol sudah <= 2, abaikan
        continue
      else:
        remove_non_terminal(start_symbol, j)  # jika masih terdapat rhs > 2, jalankan fungsi remove non terminal


# pada fungsi second_step, akan dicari rhs dari start symbol, jika > 2, jalankan fungsi dibawah
def remove_non_terminal(pin, check_non_term):
  lst_check_val = check_non_term.split(' ')  # split rhs yang akan di cek, sehingga menjadi sebuah list
  temp = ''
  index = get_subs_index(new_rs, check_non_term)
  if index == -1:
    add_val = ' '.join(lst_check_val[0:2])
    new_ls.append(var_ls[len(new_ls)])
    new_rs.append(add_val)
    temp = check_non_term.replace(add_val, new_ls[len(new_ls) - 1])
    dic.update({new_ls[len(new_ls) - 1]: [add_val]})
  else:
    temp = check_non_term.replace(new_rs[index], new_ls[index])
  dic[pin][dic[pin].index(check_non_term)] = temp


# mencari lhs yang panjang rhs > 2
def rule_max_length():
  maks = 0  # inisiasi awal var maks
  for i in dic[start_symbol]:  # perulangan untuk mencari rhs dari start symbol
    if len(i.split(' ')) > maks:  # jika panjang rhs lebih dari maks
      maks = len(i.split(' '))  # maks diisi dengan panjang dari rhs
  return maks


def get_subs_index(new_rs, check_non_term):
  for i in new_rs:
    if i in check_non_term:
      return new_rs.index(i)
  return -1


def run_conversion():
  # print('CFG: ')
  # display(dic)
  first_step()
  second_step()
  # print('CNF: ')
  # display(dic)
  return dic