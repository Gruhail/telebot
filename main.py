import telebot
from test import TOKEN_BOT, keys
from extensions import Convertor, APIException

bot = telebot.TeleBot(TOKEN_BOT)
@bot.message_handler(commands=['start', 'help'])

def help(message:telebot.types.Message):
   text = ('Чтобы начать работу введите комманду боту в следующем формате:\n<имя фолюты>'
           ' \<в какую валюту перевести> \ <количество переводимой валюты'
           '\nУвидить список всех доступных валют: /values')
   bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split()
    values = list(map(str.lower, values))
    try:
        result = Convertor.get_price(values)
    except APIException as e:
        bot.reply_to(message, e)
    except Exception as e:
        bot.reply_to(message, e)
    else:
        text = f'{values[2]} {keys[values[0]]} = {result} {keys[values[1]]}'
        bot.reply_to(message, text)






bot.polling(none_stop= True)
