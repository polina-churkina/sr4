A = input('Введите имя: ')
B = input('Введите фамилию: ')
C = int(input('Введите год рождения: '))
print(A,'_',B,'_',C)
A1 = A
A = B
B = A1
C = C+60
print(A,'_',B,'_',C)