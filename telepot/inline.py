import sys
import time
import pprint
import telepot
import os
import re
from telepot.namedtuple import InlineQueryResultArticle

# Insert your token here
bot = telepot.Bot("145378027:AAHtXELIly8RzCvdes3Key87cgfMZP53hjQ")

#Ricerca file mp3
def find(pattern):
	result = []
	path="mp3"
	for root, dirs, files in os.walk(path):
		for name in files:
			if re.search(pattern,name,re.IGNORECASE):
				result.append(name)
	return result

def handle(msg):
	flavor = telepot.flavor(msg)

	if flavor == 'normal':
		bot.sendMessage(chat_id,"Ok")
		print 'Normal message'

	elif flavor == 'inline_query':
		query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
		print from_id
		if len(query_string)>=3:
			filelist=find(query_string) 

			#print filelist
			articles=[]
			id=0
			for filename in filelist:
				articles.append(InlineQueryResultArticle(id=filename, title=os.path.splitext(filename)[0], message_text=os.path.splitext(filename)[0]))
				id+=1
			
			print articles
			bot.answerInlineQuery(query_id, articles)

	elif flavor == 'chosen_inline_result':
		print  "chosen_inline_result"
		result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
		print result_id
		print from_id
		f = open("mp3/"+ result_id, 'rb')
		#bot.sendDocument(from_id,f)
		bot.sendMessage(from_id,"Ok")
		#f.close()	
		 

bot.notifyOnMessage(handle)
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
