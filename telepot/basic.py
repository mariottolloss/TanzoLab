import sys
import time
import pprint
import telepot

def handle(msg):
    pprint.pprint(msg)

# Insert your token here
bot = telepot.Bot("145378027:AAHtXELIly8RzCvdes3Key87cgfMZP53hjQ")
bot.notifyOnMessage(handle)
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
