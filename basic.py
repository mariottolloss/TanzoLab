$ virtualenv telepot-example
$ cd telepot-example
$ source bin/activate
(telepot-example)$ pip install telepot
(telepot-example)$ mkdir project
(telepot-example)$ cd project

import telepot

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, 'ciao, sono un bot molto stupido!')

TOKEN = '*** inserisci il tuo token qui  ***'

bot = telepot.Bot(429903123:AAHg4u-3DAiNLGGOAHQPuVboQlV1gb2ti_w)
bot.message_loop(on_chat_message)

print 'Listening ...'

import time
while 1:
    time.sleep(10)
    
    (telepot-example)$ python basic.py
