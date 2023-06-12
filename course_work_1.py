from random import choices


# бонусом написал код дешифратор
# для проверки корректности перевода слова
# в программе не применял
def morse_decode(word):
    '''
    Переводит с Морзе обратно
    '''
    decode = []
    word_split = word.split(' ')
    morse_decode_alpabeth = {value: key for key, value in morse_code_alpabeth.items()}
    for letter in word_split.lower():
        if letter in morse_decode_alpabeth:
            decode.append(morse_decode_alpabeth[letter])
    return ''.join(decode)


def morse_encode(word):
    """
    Переводит слово в код Морзе
    """
    encoded = []
    for letter in word.lower():
        if letter in morse_code_alpabeth:
            encoded.append(morse_code_alpabeth[letter])
    return ' '.join(encoded)


def get_word():
    '''
    Получаем случайное слово из списка
    '''
    return (''.join(choices(decode_words_list, k=1)))


def print_statistics(answers):
    '''
    Выводим статистику
    '''
    return f'''Всего задачек: {len(answers)}
Отвечено верно: {answers.count(True)}
Отвечено неверно: {answers.count(False)}'''


# счетчик булевых значений
answers = []

# азбука Морзе
morse_code_alpabeth = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

# список слов для кодирования
decode_words_list = ['flash', 'arrow', 'smile', 'summer', 'python', 'fishing', 'fish', 'camping']

# приветсвуем пользователя
print('''Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем''')

# Запуск бесконечного цикла, пока не отработает сценарий с вопросами
while True:

# ввод Enter
    hello_check = input()

# проверка на Enter
    if hello_check == '':

    # цикл вопросов на 5 итераций
        for i in range(1, 6):

            word = get_word()

            user_question = input(f'''Слово {i} - {morse_encode(word)} ''')

            if user_question == word:
                answers.append(True)
                print(f'Верно, {word}!')

            else:
                answers.append(False)
                print(f'Неверно, {word}!')

        print(print_statistics(answers))
        break

    else:
        print('Введены символы, очистите поле и повторите')
