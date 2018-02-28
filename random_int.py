#!/usr/bin/env python3

import random
import time

# Steps:
# 0 - greet
# 1 - print elipsis, one dot per second
# 2 - print random value, 1-6 inclusive

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
	
greet()
rolldie()
