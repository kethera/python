import random
import time

# Steps:
# 0 - greet
# 1 - print elipsis, one dot per second
# 2 - print random value, 1-6 inclusive

def greet():
	print('You have rolled a ', end='', flush=True)
	return

def dots():
	for x in range(0, 3):
		time.sleep(1)
		print('. ', end='', flush=True)
	time.sleep(1)
	return

def rolldie():
	print(random.randint(1, 6))


greet()
dots()
rolldie()