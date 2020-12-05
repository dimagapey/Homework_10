filename = input('Введите название файла: ')
f = open(filename, 'w')
while True:
    s = input('Insert something: ')
    if s == '': break
    f.write(s+'\n')
f.close()