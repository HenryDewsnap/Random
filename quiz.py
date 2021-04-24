import csv
import random


with open("questions.csv", "r") as csv_file:
	questions = list(csv.reader(csv_file))

def Question(Output, Inputs):
	points = 0
	print(f"{Output}")
	for a in range(len(Inputs)):
		Q_Ans = input("-> ")
		for b in range(len(Inputs)):
			if Q_Ans.lower() == Inputs[b].lower():
				
				points += 1
				break
	return points

def QuestionManager():
	Q_Num = random.randint(0,len(questions)-1)
	return Question(questions[Q_Num][0], questions[Q_Num][1:len(questions[Q_Num])])
	##We want to pop the quesiton here

def GameManager():
	Total = 0
	Run = True
	while Run == True:
		Total += QuestionManager()

		
			
	print(f"{Total}")




QuestionManager()
