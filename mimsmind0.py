### Imports

import random
import sys


### Body

"""Try takes the length entered in the command line and converts it into an integer. If no length is given, it throws an exception where the default is 1.
"""
try:
	nr_digits = int(sys.argv[1])	
except:
	nr_digits = 1 		# If length is not provided, default = 1
	


"""This function calculates the range for the random number, picks the number, and then helps the user with hints in guessing that number. 
"""

def guess_number():
	# Set upper limit. If nr_digits=3: 10^3 = 1000.  Max number => 1000-1 = 999
	upper_limit = int((10 ** nr_digits) - 1)		
	# Set lower limit. If nr_digits=3: 10^(3-1). Min number => 10^2 = 100
	lower_limit = int(10 ** (nr_digits - 1))			
	number = random.randint(lower_limit, upper_limit)	# Range of random number
	# print number 		# Just to check what the random number is. 	
	
	# Takes first input
	print "Let's play the mimsmind0 game."
	guess = int(raw_input("Guess a {0}-digit number: " .format(nr_digits))) 
	count = 1
	

	"""This function recursively checks the value of the guess and gives hints. The program ends when the guess is correct. 
	"""
	def result(guess, count):				
		if guess < number:
			new_guess = int(raw_input("Try again. Guess a higher number: "))
			count += 1
			result (new_guess, count)		# Calls the function again to evaluate new guess
		elif guess > number:
			new_guess = int(raw_input("Try again. Guess a lower number: "))
			count += 1
			result(new_guess, count)		# Calls the function again to evaluate new guess
		else:
			print "Congratulations! You guessed the right number in {0} tries" .format(count)

	result(guess, count)					




def main():

	guess_number()


if __name__ == '__main__':
    main()

