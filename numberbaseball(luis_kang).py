import random

is_true = True
is_real = True
is_really = True
is_rreal = True

Turn = 0
store = ""

while is_real:
	print "Play Ball!"
	com_list = []
	for x in range(1, 10):
		com_list.append(x)
	random.shuffle(com_list)
	com_list_real = []
	for x in range(4):
		com_list_real.append(com_list[x])

	while is_true:
		while is_really:
			user_number = raw_input("Choose the numbers between 1 and 9 :")
			if user_number.isdigit()==False:
				print "Numbers!"
				continue

			user_lis = [int(x) for x in user_number]
			
			if len(user_lis) != 4:
				print "You should choose 4 numbers"

			elif len(user_lis) == 4:
				error_list = [int(x) for x in user_number]
				for x in range(4):
					error_number = error_list[0]
					error_list.remove(error_number)
					if error_number in error_list:
						print "All numbers should be different"
						break
				if error_list == []:
					is_really = False
		
		strike = "S"
		ball = "B"
		totalstrike = 0
		totalball = 0

		for i in range(4):
				if user_lis[i] == com_list_real[i]:
					totalstrike += 1
				elif user_lis[i] in com_list_real and user_lis[i] != com_list_real[i]:
					totalball += 1
		print str(totalstrike) + strike + "" + str(totalball) + ball
		
		if totalstrike != 4:
			Turn += 1
			is_really = True
			store += "Turn:" + str(Turn) +"\n" + "Your number : " + str(user_number) + "\n" + "Result :" + str(totalstrike) + strike + "" + str(totalball) + ball + "\n"
			print "Turn : " + str(Turn)

		elif totalstrike == 4:
			Turn += 1
			is_true = False
			store += "Turn:" + str(Turn) +"\n" + "Your number : " + str(user_number) + "\n" + "Result :" + str(totalstrike) + strike + "" + str(totalball) + ball + "\n"
			print "Turn :" + str(Turn)
			print "Congratulation!"

	print "Play again? :"
	while is_rreal:
		game_again = raw_input("[Y/N]")
		if game_again != "Y" and game_again != "N":
			print "You should choose Y or N"
		elif game_again == "Y" or game_again == "N":
			is_rreal = False

	if game_again == "Y":
		is_true = True
		is_really = True
		is_rreal = True

	elif game_again == "N":
		is_real = False
		is_rreal = False
		is_true = False
		is_really = False
		print "Well... Okay"


print "Save Game? :"
file_true = True
while file_true:
	save_file = raw_input("[Y/N] :")
	if save_file != "Y" and save_file != "N":
		print "Choose Y or N"
	elif save_file == "Y" or save_file == "N":
		file_true = False

if save_file == "N":
	print "Game Over"

elif save_file == "Y":
	f = open("game_logfile_luis.txt", "w")
	f.write("Play Ball" + "\n")
	f.write(raw_input("What's your name? :") + "\n")
	f.write(store + "\n")
	f.write("Congratulation! It's finally finished" + "\n")
	f.write("Total : Try " + "" + str(Turn) + " times" + "\n")
	f.write("Save Complete! Game Over")
	print "Save Complete! Game Over"
	f.close()