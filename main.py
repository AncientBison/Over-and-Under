import acc
import random
import dotenv
import getpass
import sys
import time
import main
from UsefulCommands import *

class var:
	def __init__():
		username = None
		money = None
v = var

def signIn():
	signin = ask("1: Make a new account\n2: Log in.\nEnter 1 or 2: ")
	if signin == "1":
		usernameinput = ask("Enter your new username (Not case sensitive) : ")
		passwordinput = getpass.getpass("Enter your new password (Case sensitive) : ")
		with open("passwords.env", "a") as pwf:
			pwf.write("{}={}\n".format(usernameinput.lower(),passwordinput))
			v.username = usernameinput
		startgame()
	else:
		usernameinput = ask("Enter your username (Not case sensitive) : ")
		passwordinput = getpass.getpass("Enter your password (Case sensitive) : ")
		with open("passwords.env", "r") as pwf:
			entries = pwf.readlines()

		secure = False
		for entry in entries:
			(username, password,v.money) = entry.split("=")
			print("asking: " + username)
			time.sleep(0.08)
			print(Clear)
			if username.lower() == usernameinput.lower() and password == passwordinput:
				secure = True
				for i in range(3):
					sys.stdout.write(Green + '\rSUCCESS' + Reset)
					time.sleep(0.5)
					sys.stdout.write('\r       ')
					time.sleep(0.5)
				v.username = usernameinput
				startgame()

		if not secure:
			for i in range(3):
				sys.stdout.write(Red + '\rFAIL')
				time.sleep(0.5)
				sys.stdout.write('\r    ')
				time.sleep(0.5)
			sys.exit()

class deck:
	def __init__(self):
		self.cards = []
		for i in range(1,5):
			for num in range(1,11):
				self.cards.append(num)
		random.shuffle(self.cards)
	def draw(self):
		return self.cards.pop(0)
d = deck

def startgame():
	print(Clear)
	print("Welcome " + v.username + " to UDGambling!")
	print("The rules are: \n1: Draw 2 cards.\n2: Play a card on your opponent.\n3:Your opponenet must play a card 1 over, 1 under, or the exact same to pass\n4: If your opponent does not have the cards to do that then they must pick up a fail token")

signIn()