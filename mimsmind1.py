

import random
import sys

try:
	nr_digits = int(sys.argv[1])	
except:
	nr_digits = 3 			# Default length of number is 3


"""The user is asked for a number and based on that, the range of random number and number of rounds is calculated. The user is prompted to enter his/her guess. 
"""
def guess_number():
	maxrounds = (2**nr_digits) + nr_digits

	upper_limit = int((10 ** nr_digits) - 1)		
	lower_limit = int(10 ** (nr_digits - 1))	# "{0:0>nr_digits}".format(0) not working
	number = str(random.randint(lower_limit, upper_limit))	# Converted to string because we want to traverse through each item of the string
	# print number
	print "Let's play the mimsmind1 game. You have {0} guesses." .format(maxrounds)
	guess = raw_input("Guess a {0}-digit number: " .format(nr_digits))  # Already a string
	count = 0

	
	"""This function evaluates the user's guess and gives hints till the correct number is guessed. However, the game is over if maximum rounds are reached.
	"""
	def bulls_cows(x):
		try:
			int_guess = int(guess) and len(guess) == nr_digits  # Try checks whether the length of the number entered is right and that only numbers are entered. 
		except:
			guess = raw_input("Invalid input. Try again: ")
			count += 1 		

		b = 0  		# Initialize bull count
		c = 0		# Initialize cow count
		i = 0		# Initialize index count

		for digit in guess:		# Traverses every digit in 'guess'. If the digit is in the same index as 'number', gives 1 Bull. If the digit is in another index in 'number', gives 1 Cow. With each letter, 'i' is increased by 1 to keep moving to the next index  'number'. 
			if digit == number[i]: 
				b += 1 		# Increases for every number matched in the right index
				i += 1
				
			elif digit in number:
				c += 1  	# Increases for every number matches in the original number. 
				i += 1	

		if count == maxrounds:		# Game over when max. lives are used. 
				print "Sorry! You're out of your {0} lives." .format(maxrounds)
				sys.exit()
		elif b == nr_digits:
			print "Congrats! You guessed it in {0} tries." .format(count)	
		else:
			g = raw_input("{0} bull(s), {1} cow(s). Try again: " .format(b, c))
			count += 1
			bulls_cows(g)	# Recursion passes g, the new guess through the bull_cows function. 
	bulls_cows(guess)		
		

guess_number()

