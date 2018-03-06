#!/usr/bin/env python3
<<<<<<< HEAD
=======

>>>>>>> 47e29b892845fe60aa461417437fa8e590b54cee
import random
import time

# Single random-number generator "Roll the die"
#
# Steps:
# 1 - Greet and input the number of sides into a variable
# 2 - Print as many periods for "thinking time" but only a max of seven (it seemed good)
# 3 - Print the random value

<<<<<<< HEAD

def dots(x):
	if x>7:
		x=7
	for x in range(0, x):
		time.sleep(1)
		print('. ', end='', flush=True)
	time.sleep(1)
	return

sides=int(input("Hello, how many sides would you like on your die? "))
print('You have rolled a ', end='', flush=True)
dots(sides)
print(random.randint(1, sides))
=======
def greet():
	print('\nRolling the single-sided die now!', flush=True)
	return

def dots():
	for x in range(0, 3):				# Do this loop 3 times
		time.sleep(1)					# Sleep one second per loop iteration
		print('. ', end='', flush=True) # Print a full stop, no \n, flush terminal
	time.sleep(1)						# Wait one more second after the loop
	return

def rolldie():
	print('\nYou rolled a ', end='', flush=True)
	dots()
	print(random.randint(1, 6),('\b!\n'))  # Display the random value, backspace, new line
	return
	
	
greet()
rolldie()
>>>>>>> 47e29b892845fe60aa461417437fa8e590b54cee
