'''
Hopkins Computer Science Club Signup Program
By: Alexander Aron (2015)
Feel free to use this program for signup in the future :)
'''

#define a screen clearing function
import os
clear = lambda: os.system('clear') #replace 'clear' with 'cls' for windows

#signup
while (1==1): #infinite loop
	clear()
	print "\nPlease enter your information below if you would like to join the Hopkins Computer Science Club." #the escape sequence '\n' creates a new line
	name = raw_input("\nWhat is your name? \n") #raw_input() is different from input(). the former accepts any type of input whereas the ladder only accepts numbers and (i believe) characters
	email = raw_input("\nWhat is your email address? \n")
	comment = raw_input("\nFeel free to leave a comment:\n")

	#write all data to file
	f = open("list.txt","a") #open file with the 'a' parameter, meaning we want to write but not overwrite the file
	f.write(name + "    " + email + "    " + comment + "\n")
	f.close() #close file for safety

	#write email list formatted for copy+paste into google groups
	f = open("emails.txt","a")
	f.write(email + ", ")
	f.close()

	print "\nThank you for signing up! We will email you soon with club information."
	raw_input("Press enter to refresh the screen. ") #after enter is pressed, the loop restarts