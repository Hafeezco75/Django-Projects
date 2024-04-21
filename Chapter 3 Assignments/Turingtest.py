Enter = next 

answer = "yes"

solution = "no"

UserInput = str(input("what is your problem? "))

while (UserInput == Enter):

	continue

Users = str(input("Have you had this problem before(yes or no)? "))

if (Users == answer):

	print('Well, you have it again.')

elif(Users == solution):

	print('Well,you have it now')

