 for i in range(1, 4):  # for i in range(3)
     for j in range(4):
         print('*', end='')
     print()
#
#
# # i가 0이거나 마지막이면 => 찍는다
# # (i가 0이 아니고 마지막이 아니면) and (j가 0이거나 마지막이면) => 찍는다
# # 이 경우가 아니면 " " 를 찍는다
 for i in range(4):
     for j in range(4):
         if i == 0 or i == 3:
             print('*', end='')
         elif (i != 0 and i != 3) and (j == 0 or j == 3):
             print('*', end='')
         else:
             print(' ', end='')
     print()


