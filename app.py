import time
import string
import multiprocessing as mp
import numpy as np;
from math import log;


def combinations(digits,cores=1):

	length  = len(string.ascii_lowercase);
	combination = "a"*digits
	if(cores == 1):
		#end = length**digits
		counter = 1;
#print(length**digits);
		for i in range(0, (length**digits)):
	#subtract = float(log((i+1), length));
	#whole number
	#if(subtract % 1A == 0):
		#print("Log: "+str(subtract));
	#first digit
			yield combination
	#actual_string = combination.copy();
			if((i+1)%26 == 0):
				counter = 0;
			for x in range(1, digits):
				if((i+1)%(length**x) == 0):
					counter =0;
			#get the second to last digit
					second_to_last_digit = combination[digits-x-1]
			#"a" --> "b" -->"c" -->"d"
			#if(string.ascii_lowercase.index(second_to_last_digit) == "z"):
					index = int(string.ascii_lowercase.index(second_to_last_digit)) + 1;
					if(index < 26):
						new_char = string.ascii_lowercase[index]
					else:
						index = 0;
						new_char = string.ascii_lowercase[index]
				#combination = combination[:x] + (new_char*(digits-x))
					if(digits -x-1 == 0):
						combination = new_char + combination[digits-x:digits]
				#print("This has been triggered");
					else:
						combination = combination[:digits-x-1]+new_char + combination[digits-x:digits]
				#print(combination);
			if(digits-1 == 0):
				combination = string.ascii_lowercase[counter]
			else:
				combination = combination[:digits-1] + string.ascii_lowercase[counter]
			counter+=1;

#print(len(lets));
