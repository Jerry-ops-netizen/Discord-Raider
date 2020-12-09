import tkinter as tk
from tkinter import ttk
from tkinter import * 
import threading
import requests
import time
import webbrowser
import json
import random
import os

os.system("title Spam Es Divertido - github.com/kieronia")

spamnow = False
#lines = open('proxies.txt').read().splitlines()
def livemessage():
	global finalmessage
	global finalid
	
	while True:
		try:
			messagetospam = message.get()
			finalmessage = messagetospam.strip()
			channelidtouse = channelids.get()
			finalid = channelidtouse.strip()
		except:
			pass




def spem(line,number):
	global lines
	global finalmessage
	global finalid
	global spamnow
	token = line.strip()
	headers = {'Authorization': token}

	while True:	
		if spamnow == True:
			
			#proxy =random.choice(lines)
			#proxies = {'https': 'https://%s' % (proxy)}
			try:
				#messagesend = requests.post(f"https://discord.com/api/v8/channels/{finalid}/messages",json={'content': finalmessage}, headers=headers, proxies = proxies)
				messagesend = requests.post(f"https://discord.com/api/v8/channels/{finalid}/messages",json={'content': finalmessage}, headers=headers)
			
				if messagesend.status_code == 200:
					print(f"[{number}]  Message Sent [{token}]")
				else:
					print(f"[{number}]  Error Sending Message [{token}]")
			except:
				print(f"[{number}]  Proxy Error [{token}]")
			
		time.sleep(0.1) #tkinter is extremely laggy, this was needed or it'd go crazeeee
			




def start():
	global spamnow
	spamnow = True


def stop():
	global spamnow
	spamnow = False


def spamisfun():
	print("[>] Opening spamis.fun")
	webbrowser.open("https://spamis.fun/")



root = Tk()

root.geometry('658x414')
root.configure(background='#f9f9f9')
root.title('Server Spammer - Spam es divertido')


Label(root, text='Server Spammer', bg='#FFFFFF', font=('arial', 12, 'bold')).place(x=256, y=31)


channelids=Entry(root)
channelids.place(x=252, y=114)


message=Entry(root)
message.place(x=252, y=210)


Button(root, text='Start', bg='#FFFFFF', font=('arial', 20, 'bold'), command=start).place(x=94, y=337)


Button(root, text='Stop', bg='#FFFFFF', font=('arial', 20, 'bold'), command=stop).place(x=411, y=330)


Label(root, text='Channel ID:', bg='#FFFFFF', font=('arial', 10, 'normal')).place(x=252, y=90)


Label(root, text='Message:', bg='#FFFFFF', font=('arial', 10, 'normal')).place(x=252, y=188)


Button(root, text='Visit the OFFICIAL spamis.fun', bg='#FCFCFC', font=('arial', 10, 'bold'), command=spamisfun).place(x=422, y=0)

with open("tokens.txt", 'r') as f:
	number = 0
	for line in f.readlines():
		number = number + 1
		threading.Thread(target = spem, args = (line,number,)).start()


threading.Thread(target = livemessage).start()









root.mainloop()
