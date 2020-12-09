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




def join(line,number):
	global serverlink
	token = line.strip()
	headers = {'Authorization': token}


	try:
		joining = requests.post(f"https://discord.com/api/v8/invites/{serverlink}", headers=headers)
			
		if joining.status_code == 200:
			print(f"[{number}] Successfully Joined discord.gg/{serverlink} [{token}]")
		else:
			print(f"[{number}]  Error Joining discord.gg/{serverlink} [{token}]")
	except:
		print(f"[{number}]  Connection Error [{token}]")
			
			




def start():
	global serverlink
	serverlink = discordlink.get()
	serverlink = serverlink.replace("https://discord.gg/","")
	serverlink = serverlink.replace("discord.gg/","")
	serverlink = serverlink.replace("https://discord.com/invite/","")
	serverlink = serverlink.replace("https://discord.com/","")
	#print(serverlink)
	with open("tokens.txt", 'r') as f:
		number = 0
		for line in f.readlines():
			number = number + 1
			threading.Thread(target = join, args = (line,number,)).start()




def spamisfun():
	print("[>] Opening spamis.fun")
	webbrowser.open("https://spamis.fun/")



root = Tk()

root.geometry('658x414')
root.configure(background='#f9f9f9')
root.title('Server Spammer - Spam es divertido')


Label(root, text='Server Joiner', bg='#FFFFFF', font=('arial', 12, 'bold')).place(x=256, y=31)


discordlink=Entry(root)
discordlink.place(x=252, y=114)




Button(root, text='Start', bg='#FFFFFF', font=('arial', 20, 'bold'), command=start).place(x=272, y=200)



Label(root, text='Invite Link:', bg='#FFFFFF', font=('arial', 10, 'normal')).place(x=252, y=90)




Button(root, text='Visit the OFFICIAL spamis.fun', bg='#FCFCFC', font=('arial', 10, 'bold'), command=spamisfun).place(x=422, y=0)











root.mainloop()
