user_input_word = input('Введите слово: ').lower()
if user_input_word == user_input_word[::-1]:
    print('Да, это слово палиндром')
else:
    print('Введенное слово е является палиндромом')
