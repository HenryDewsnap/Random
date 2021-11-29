morse_code_data = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.", "q" :"--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..", " ": "  ", "  ": " "}

def swapKeys(setToSwap): ##Swaps the key:data of the dictionary set and returns it.
	swap = {}
	for key in setToSwap:
		swap[setToSwap[key]] = key
	return swap

def translate(convType, message): ##Takes the conversion type [e/m] and a message and returns the english or morse code data.
	output = ""
	if convType == "m": char_set = swapKeys(morse_code_data)
	else: char_set = morse_code_data
	
	if convType == "e": 
		for char in list(message): output += f"{char_set[char]} "
	else:
		for word in message.split(" "): output += char_set[word]
	return output

def main():
	print(translate(input("English to Morse / Morse To English [E/M]: ").lower(), input("Message: ").lower()))

if __name__ == "__main__": main()
