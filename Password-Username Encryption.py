import hashlib

def Main():

	if input("Do you have an account [y/n] -> ").lower() == "y":
		User_P, Pass_P = UserInput() ##_P means plain text
		AccountVeri(User_P, Pass_P)

	else:
		GenerateAcc()


def AccountVeri(User_P, Pass_P):
	User_H = Hasher(User_P)
	Pass_H = Hasher(Pass_P)


def GenerateAcc():
	User_P, Pass_P = UserInput()
	User_H = Hasher(User_P)
	Pass_H = Hasher(Pass_P)
	SaveData(User_H, Pass_H)

def SaveData(User_H, Pass_H):
	print()




def UserInput():
	User = input("Please enter a user: ")
	Pass = input("Please enter a pass: ")
	return User,Pass



def Hasher(data):
	hash_object = hashlib.md5(data.encode())
	return hash_object.hexdigest()


Main()
