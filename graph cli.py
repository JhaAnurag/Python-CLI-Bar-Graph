import random
#import sys
import os
import time

length = 20  # Length of the list
min_value = 0  # Minimum value of the integers
max_value = 9  # Maximum value of the integers

mode = 2
space_char_Y = "─" #"─" "▔" "_"
space_char_X = "│ "
bar_char = "█"
border_sep_char = " "


def is_even(n):
    return n & 1 == 0

while True:
	l = [random.randint(min_value, max_value) for _ in range(length)]
	os.system("cls")
	print(l)
	
	h=max(l)

	length=len(l)
	width=len(str(length))+1
	mid=(width//2)


	print(" Y"+"┌──"+border_sep_char.join(map(lambda x: str(abs(x-h)).zfill(width-1), range(h)))+"─"*(width-1)+"┐")
	for index, element in enumerate(l):
		adjustment = 0
		if is_even(element): adjustment = 1
		print(str(index+1).zfill(width-1)+"│"+"─",end="")
		print(bar_char*(element)*(width)+str(element).zfill(width-1)+" "*adjustment+space_char_X*((h-element)//2)*(width)+space_char_X*(adjustment+1)+str(length-index).zfill(width-1))
	print("0"*(width-1)+"└──"+border_sep_char.join(map(lambda x: str(x+1).zfill(width-1), range(h)))+"─"*(width-1)+"┘X")

	#print()

	print(" "*(width-2)+"Y"+"┌─"+border_sep_char.join(map(lambda x: str(abs(x-length)).zfill(width-1), range(length)))+"─"*(width-2)+"┐")
	for i in range(h+1):
		print(str(h-i+1).zfill(width-1)+"│"+space_char_Y, end="")
		for index,j in enumerate(l):
			if j < h:
				print(space_char_Y*width, end="")
			elif j == h:
				print(str(j-i).zfill(width-1)+space_char_Y*(width-mid-1), end="")
			else:
				if mode == 0:
					print(bar_char*width, end="")
				if mode == 1:
					print(space_char_Y*(mid)+bar_char+space_char_Y*(width-mid-1), end="")
				if mode == 2:
					print(bar_char*(mid+1)+space_char_Y*(width-mid-1), end="")
			l[index]+=1
		print("│"+str(i+1).zfill(width-1),end="")
		print()
	print("0"*(width-1)+"└─"+border_sep_char.join(map(lambda x: str(x+1).zfill(width-1), range(length)))+"─"*(width-2)+"┘X")
	print()
	time.sleep(1)

#print("    "+"-"*(length*width-1)+"   ")
#print([i for i in range(length)])
#"pattern printing questions like: "--  --  --"
#data formatting to fit in graph
#adding custom x labels
# auto border around passed print statement wiht labels
