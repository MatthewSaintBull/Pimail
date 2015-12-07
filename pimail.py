import os
import sys
import time
import feedparser


try : 
	SERVER="mail.google.com"
	PATH="/gmail/feed/atom"
	LED_RED = 17
	LED_GREEN = 22
	N = 5
	I = 0
	TEMPO = 3
	MAIL_C = 0
	NUOVE_MAILS = 0
	USR = raw_input("Insert email : ")
	PWD = raw_input("Insert Password : ")
	
	os.system('clear')

	print 'WELCOME IN THE MAIL CLIENT!!!'
	print 'MADE BY MATTEO SANTORO'

	while (I < N):
		os.system('gpio -g mode 17 out')
		os.system('gpio -g mode 17 in')
		os.system('gpio -g mode 22 out')
		os.system('gpio -g mode 22 in')
		I += 1

	time.sleep(2)
	
	NUOVE_MAIL = feedparser.parse("https://" + USR + ":" + PWD + "@" + SERVER + PATH)
	
           
	while 1:
		NUOVE_MAILS = int(feedparser.parse("https://" + USR + ":" + PWD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
	 
		if NUOVE_MAILS > MAIL_C :
	
			os.system('gpio -g mode 22 out')
			os.system('gpio -g mode 17 in')
			print 'YOU HAVE ' + str(NUOVE_MAILS) + ' MAILS UNREAD!!'
			
		else :
			os.system('gpio -g mode 17 out')
			os.system('gpio -g mode 22 in')
			print "YOU DON'T HAVE ANY MAIL UNREAD"
	
		time.sleep(TEMPO)


except KeyboardInterrupt:
	os.system('gpio -g mode 17 in')
	os.system('gpio -g mode 22 in')
	os.system('clear')
	if NUOVE_MAILS > MAIL_C :
		print '\n\nMAILS UNREAD : '

        	for i in xrange(len(NUOVE_MAIL.entries)):
		        print ""
		        print 'AUTHOR : ' + NUOVE_MAIL.entries[i].author_detail.email
		        print 'SUBJECT : ' + NUOVE_MAIL.entries[i].title
		        print 'BODY :  \n' + NUOVE_MAIL.entries[i].summary_detail.value
			print '-----------------------------'
		print '\n\n[[!!END SCRIPT!!]]'
	else:
		print '[!!END SCRIPT!!]]'

