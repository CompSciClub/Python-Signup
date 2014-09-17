'''
Hopkins Computer Science Club Signup Program
By: Alexander Aron (2015)
Feel free to use this program for signup in the future :)
'''

#define a screen clearing function
import os
clear = lambda: os.system('clear') #replace 'clear' with 'cls' for windows

#signup
while (True): #infinite loop
	clear()
	fname = raw_input("What is your first name? \n") #raw_input() is different from input(). the former accepts any type of input whereas the ladder only accepts numbers and (i believe) characters
	lname = raw_input("\nWhat is your last name? \n")
	grade = raw_input("\nWhat is your graduation year? (ex: 2015) \n")
	comment = raw_input("\nFeel free to leave a comment:\n")

	#generate hopkins email
	email = fname[0].lower() + lname.lower() + grade[2] + grade[3] + "@students.hopkins.edu"

	#write all data to file
	f = open("list.txt","a") #open file with the 'a' parameter, meaning we want to write but not overwrite the file
	f.write(fname + " " + lname +  "    " + email + "    " + comment + "\n")
	f.close() #close file for safety

	#write email list formatted for copy+paste into google groups
	f = open("emails.txt","a")
	f.write(email + ", ")
	f.close()

	print "\nThank you for signing up! We will email you soon with club information."
	raw_input("Press enter to refresh the screen. ") #after enter is pressed, the loop restarts