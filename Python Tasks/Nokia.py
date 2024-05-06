menuprompt = """\t Welcome to Menu.....
     Press 
     1 -> Phonebook
     2 -> Messages
     3 -> Chat
     4 -> Call Register
     5 -> Tones
     6 -> Settings
     7 -> Call Divert
     8 -> Games
     9 -> Calculator
    10 -> Reminders
    11 -> Clock
    12 -> Profiles
    13 -> SIM services"""

print(menuprompt)

MENU = int(input("Hello Nokia,Welcome to Menu"))

match MENU:
	case 1: print("Phonebook")
 
	case 2: print("Messages")

	case 3: print("Chat")

	case 4: print("Call Register")

	case 5: print("Tones")

	case 6: print("Settings")

	case 7: print("Call Divert")
 
	case 8: print("Games")

	case 9: print("Calculator")

	case 10: print("Reminders")

	case 11: print("Clock")

	case 12: print("Profiles")

	case 13: print("SIM services")

PHONEBOOK = int(input("Hello,Welcome to Phonebook"))

phonebook = """\t Choose any of the Phonebook Options
      Press
      1 -> Search
      2 -> Service Nos
      3 -> Add name
      4 -> Erase
      5 -> Edit
      6 -> Assign tone
      7 -> Send b'card
      8 -> Options
      9 -> Speed dials
     10 -> Voice tags"""

print(phonebook)

match PHONEBOOK:
	case 1:print("Search")

	case 2:print("Service Nos")

	case 3:print("Add name")

	case 4:print("Erase")

	case 5:print("Edit") 

	case 6:print("Assign tone")  
	
	case 7:print("Send b' card")

	case 8: print("Options")

OPTIONS = int(input("Welcome to Options,choose the available options"))

match OPTIONS:
	case 1: print("Type of view")
        
	case 2: print("Memory status")
 
	case 9: print("Speed dials")

	case 10: print("Voice tags")


MESSAGES = int(input("Welcome to Messages,Click the available options"))

match MESSAGES:
	case 1: print("Write messages")

	case 2: print("Inbox")
	
	case 3: print("Outbox")

	case 4: print("Picture messages")

	case 5: print("Templates")

	case 6: print("Smileys")

SETTINGS = int(input("This is Message Settings,Choose from the Options"))

match SETTINGS:
	case 1: print("Set")

	case 2: print("Common")

SET = int(input("choose the Options below"))

match SET:
	case 1: print("Message centre number")

	case 2: print("Messages sent as")

	case 3: print("Message validity")
      

match COMMON:
	case 1: print("Delivery reports")

	case 2: print("Reply via same centre")

	case 3: print("Character support")

	case 8: print("Info service")

	case 9: print("Voice mailbox number")
 
	case 10: print("Service command editor")

match CALLREGISTER:

	case 1: print("missed calls")

	case 2: print("received calls")

	case 3: print("dialled numbers")
            	
	case 4: print("Erase recent call lists")

	case 5: print("Show call duration")

match SHOWCALLDURATION:

	case 1: print("Last call duration")
            	     
	case 2: print("All calls' duration")

	case 3: print("Received calls duration")

	case 4: print("Dialled calls duration")

	case 5: print("Clear timers")


	case 6: print("Show call costs")

match SHOWCALLCOSTS:

	case 1: print("Last call cost")

	case 2: print("All calls'cost")

	case 3: print("Clear counter")

match CALLCOSTSETTINGS:

	case 7: print("Call cost settings")

	case 1: print("Call cost limit")
	
	case 2: print("Show costs in")



	




             

