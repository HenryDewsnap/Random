//FOR THIS CODE TO WORK YOU MUST HAVE A .csv WITH QUOTES IN IT SEPERATED BY COMMAS WITH NO SPACINGS UNECISSARILY USED AFTER OR BEFORE COMMAS. (file location must be in the same folder as the program.)

import random
import csv

FileName = "Quotes.csv"
TotalQuotes = 3

def INIT():
	global data
	with open('Quotes.csv', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)
	Q_Amm = Menu()
	Question(Q_Amm)

def Question(Q_Amm):
	for i in range(Q_Amm):
		Q = data[0][random.randint(0,TotalQuotes-1)]
		Q = Q.split()
		Missing_Wrd = random.randint(0,len(Q)-1)
		for a in range(len(Q)-1):
			if a == Missing_Wrd:
				print("#####", end = " ")
				continue
			print(Q[a], end = " ")
		print()
		
		if input("Input what the missing word is -> ") == Q[Missing_Wrd]:
			print("Congratulations!")
			continue

		print("Unlucky")

def Menu():
	print("Quote Tester - By: HenDewsnap")
	print(f"The file being read is [{FileName}]")
	return int(input("How many questions would you like to be asked -> "))
INIT()
