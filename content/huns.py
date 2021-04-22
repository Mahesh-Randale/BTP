import hunspell
import os

curr_dir = os.getcwd()
print(curr_dir)
dir1 = curr_dir + '/dictionary'
print(dir1)
h = hunspell.Hunspell('en_US' , hunspell_data_dir=dir1)
print("Word Suggestions ready")

while(True):
	i = input("String?")
	list1 = h.suggest(i)
	print(list1)
	list2 = []
	for s in list1:
		if s.startswith(i):
			list2.append(s)
	print(list2)
