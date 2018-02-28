#!/usr/bin/env python3

import time

#Function definitions

def first_wait():
	x=8
	for n in range(0, 6):
		print('There are',x,'minutes left.')	# Do this loop 6 times (6 mins)
		time.sleep(10)							# Sleep one minute per loop iteration
		x - 1
	return

def min_six():									# With two minutes left, egg the user on
	print('Only two minutes left now!')
	time.sleep(10)
	return

def min_seven():
	print('Just sixty seconds to go!')			# One minute warning!
	time.sleep(10)
	return


print('The Alton Brown egg timer!')
input('Boil egg(s) in kettle. Hit enter when the kettle shuts itself off')

first_wait()
min_six()
min_seven()

print('Hooray your eggs are cooked, enjoy!')

