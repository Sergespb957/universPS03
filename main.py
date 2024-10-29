import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    translator = Translator()  # Создаем экземпляр переводчика
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский
        translated_word = translator.translate(word, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        # Начинаем игру
        print(f"Значение слова на русском - {translated_definition}")
        user = input("Что это за слово? ")
        if user.lower() == translated_word.lower():  # Сравниваем с учётом регистра
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

# Запускаем игру
word_game()
