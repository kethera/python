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
	for x in range(0, 3):
		time.sleep(1)
		print('. ', end='', flush=True)
	time.sleep(1)
	return

def rolldie():
	print('\nYou rolled a ', end='', flush=True)
	dots()
	print(random.randint(1, 6),('\b!\n'))

greet()
rolldie()
