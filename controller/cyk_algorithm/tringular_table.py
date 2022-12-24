empty = '\u2205'

# mencari string terpanjang
def get_max_length(filling_table):
  max_length = -1 # inisiasi awal max = -1
  for i in filling_table:
    temp = len(max(i, key=len))
    if temp > max_length:
      max_length = temp
  return max_length


# print filling_table pada terminal
def print_table(filling_table):
  print('FILLING TABLE')
  max_length = get_max_length(filling_table) + 5

  for j in range(len(filling_table)):
    i = 0
    upper_bound = (j + 1) * max_length * '-' + (i + 2) * '-'
    print(upper_bound)
    print(end=' | ')
    for k in range((len(filling_table) -1) - j, len(filling_table)):
      if filling_table[i][k] == 'set()':
        filling_table[i][k] = empty
        print(empty.center(max_length), end=' | ')
      else:print(str(filling_table[i][k]).center(max_length), end=' | ')
      i += 1
    print()
  print(len(filling_table) * max_length * '-' + (len(filling_table) + 1) * '-')
