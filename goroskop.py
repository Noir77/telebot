# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot

import requests
from bs4 import BeautifulSoup
# Указываем токен
bot = telebot.TeleBot('1494075541:AAHpeEGuBTE3TU2Rwn7C6B_q28_b34U7X3E')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Меню»
    if message.text == "Меню" or message.text == "/start":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='oven')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='telec')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='twins')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='rack')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='lev')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='deva')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='vesi')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='skorpion')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='strel')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='koz')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='vod')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='ribi')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Меню")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "oven":
         # Формируем гороскоп
        url = "https://goroskop365.ru/aries/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "telec":
        url = "https://goroskop365.ru/taurus/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "twins":
        url = "https://goroskop365.ru/gemini/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "rack":
        url = "https://goroskop365.ru/cancer/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "lev":
        url = "https://goroskop365.ru/leo/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "deva":
        url = "https://goroskop365.ru/virgo/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "vesi":
        url = "https://goroskop365.ru/libra/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "skorpion":
        url = "https://goroskop365.ru/scorpio/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "strel":
        url = "https://goroskop365.ru/sagittarius/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "koz":
        url = "https://goroskop365.ru/capricorn/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "vod":
        url = "https://goroskop365.ru/aquarius/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    else:
        url = "https://goroskop365.ru/pisces/"
        response=requests.get(url)
        html=response.text
        soup=BeautifulSoup(html, "html.parser")
        conteiner=soup.find("div", {"class":"content_wrapper horoborder"})
        msg=conteiner.find("p")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)    
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
