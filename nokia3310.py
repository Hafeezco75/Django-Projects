def mainMenu():
	print("""
		1 : Phonebook
		2 : Messages
		3 : Chat
		4 : Call register
		5 : Tones
		6 : Settings
		7 : Call divert
		8 : Games
		9 : Calculator
		10: Reminders
		11 : Clock
		12 : Profiles
		13 : SIM Services
		""")

	menu = int(input('Welcome to Nokia 3310 Menu,Select from the list of Menu Options'))
	match(menu):
		case 1 : Phonebook()
		case 2 : Messages ()
		case 3 : Chat()
		case 4 : Callregister()
		case 5 : Tones()
		case 6 : Settings()
		case 7 : Calldivert()
		case 8 : Games()
		case 9 : Calculator()
		case 10 : Reminders()
		case 11 : Clock()
		case 12 : Profiles()
		case 13 : SimService()
     

def Phonebook():
	print("""
	1 : Search
	2 : Service nos
	3 : Add name 
	4 : Erase
	5 : Edit
	6 : Assign tone
	7 : Send b card
	8 : Options
	9 : Speed dials
	10 : Voice tags
		""")
        
	phone = int(input('enter any options in phonebook'))
	match(phone):
		case 1 : print("Search")
		case 2 : print("Service nos")
		case 3 : print("Add name")
		case 4 : print("Erase")
		case 5 : print("Edit")
		case 6 : print("Assign tone")
		case 7 : print("Send b card")
		case 8 : print("Options")
		case 9 : print("Speed dials")
		case 10 : print("Voice tags")
	
def Options():
	print("""
	1 : type of view 
	2 : memory status
		""");

	option = int(input('Choose from the Options available'))
	match(option):
		case 1 : print("Type of view");
		case 2 : print("Memory status");

def Messages():
	print("""
	1 : Write messages
	2 : inbox
	3 : Outbox 
	4 : Picture messages
	5 : Templates
	6 : Smileys
	7 : Message settings 
	8 : Info service
	9 : voice mailbox number
	10 : Service command editor
		""")

	message = int(input("kindly select out of the above options"))
	match(message):
		case 1 : print("Write messages") 
		case 2 : print("Inbox")
		case 3 : print("Outbox")
		case 4 : print("Picture messages")
		case 5 : print("Template") 
		case 6 : print("Smileys") 
		case 7 : messagesettings() 
		case 8 : print("info service") 
		case 9 : print("Voice mailbox number") 
		case 10 : print("Service command editor")
 
def messagesettings():
	print("""
	1 : Set()
	2 : Common()
	     """)

	messageset = int(input("select any of the above requirement"))
	match(messageset):
		case 1 : print("Set")
		case 2 : print("Common")

def Set():
	print("""
	1 : message centre number
	2 : message sent as
	3 : message validity
		""")

	messagesets = int(input("Click on the Available Options"))
	match(messagesets):
		case 1 : print("message centre number")
		case 2 : print("message sent as")
		case 3 : print("message validity")

def Common():
	print("""
	1 : Delivery reports
	2 : Reply via same centre 
	3 : Character support
		""")

	common = int(input('Click from the available options'))
	match(common):
		case 1 : print("delivery reports")
		case 2 : print("reply via same centre")
		case 3 : print("charcter support")

def Chat():
	print("""
	1 : Chat
	    """)

	chats = int(input("select any options"))
	match(chats):
		case 1: print("Chat")
		
def Callregister():
	print("""
	1 : Missed call
	2 : Received call
	3 : Dialled numbers
	4 : Erase recent calls lists
	5 : Show call duration
	6 : Show call costs
	7 : Call cost settings
	8 : Prepaid credit
		""")

	callregister = int(input("kidly select any options from the above"))
	match(callregister):
		case 1 : print("Missed calls")
		case 2 : print("Received calls")
		case 3 : print("Dialled numbers")
		case 4 : print("Erase recent calls lists")
		case 5 : showCallDuration()
		case 6 : showCallsCost()
		case 7 : callCostSettings()
		case 8 : print("Prepaid credit")

def showCallDuration():
	print("""
	1 : Last Call duration
	2 : all calls duration
	3 : Received Call duration
	4 : Dialled Calls duration
	5 : Clear Timers
		""")

	callduration = int(input("Enter any Options available"))
	match(callduration):
		case 1 : print("Last call duration")
		case 2 : print("All calls duration")
		case 3 : print("Received call duration")
		case 4 : print("Dialled calls duration")
		case 5 : print("Clear timers")

def showCallsCost():
	print("""
	1 : Last call cost
	2 : All calls cost
	3 : Clear counters
		""")

	callcost = int(input('Select the Options of your Choice'))
	match(callcost):
		case 1 : print("Last Call cost");
		case 2 : print("All Call cost");
		case 3 : print("Clear counters");

def callcostsettings():
	print("""
	1 : Call cost limit
	2 : Show cost in
		""")

	callcost = int(input("enter any selection of your choice"))
	match(callcost):
		case 1 : print("Call cost limit")
		case 2 : print("Show cost in")
def Tones():
	
	print("""
	1 : Ringing tone
	2 : Ringing volume
	3 : Incoming call alert
	4 : Composer
	5 : Message alert tone
	6 : Keypad tones
	7 : Warming and gaming tones
	8 : Vibrating alert
	9 : ScreenSaver
		""")

	tones = int(input("enter any of the options below"))
	match(tones):
		case 1 : print("Ringing tone")
		case 2 : print("Ringing volume")
		case 3 : print("Incoming call alert")
		case 4 : print("Composer")
		case 5 : print("Message alert tone")
		case 6 : print("Keypad tones")
		case 7 : print("Warming and gaming tones")
		case 8 : print("Vibrating alert")
		case 9 : print("Screensaver")

def settings ():
	print("""
	1 : Call settings
	2 : Phone settings
	3 : Security setiings
	4 : Restore factory settings
	      """)

	sett = int(input("enter any number of your choice"))
	match(sett):
		case 1 : callsettings()
		case 2 : phonesettings()
		case 3 : securitysettings()
		case 4 : print("Restore factory settings")

def callsettings ():
	print("""
	1 : Automatic redial
	2 : Speed dials
	3 : Call waiting options
	4 : Own number sending
	5 : Phone line in use
	6 : Automatic answer
		""")

	callset = int(input("enter any selcted options from the above"))
	match(callset):
		case 1 : print("Automatic redial")
		case 2 : print("Speed dials")
		case 3 : print("Call waiting options")
		case 4 : print("own number sending")
		case 5 : print("Phone line in use")
		case 6 : print("Automatic answer")

def phonesettings():
	print("""
	1 : language
	2 : cell info display
	3 : welcome note
	4 : network selection
	5 : lights
	6 : confirm sim service actions
		""")

	phonesett = int(input("enter any options"))
	match(phonesett):
		case 1 : print("Language")
		case 2 : print("Cell info display")
		case 3 : print("Welcome note")
		case 4 : print("Network selection")
		case 5 : print("Lights")
		case 6 : print("Confirm sim service")

def securitysettings ():
	print("""
	1 : Pin code request
	2 : Call barring service
	3 : Fixed dialling
	4 : Closed user group
	5 : Phone security
	6 : Change access codes
	    """)
	
	security = int(input("Select any of the options"))
	match(security):
		case 1 : print("Pin code request")
		case 2 : print("Call barring service")
		case 3 : print("Fixed dialling")
		case 4 : print("Closed user group")
		case 5 : print("Phone security settings")
		case 6 : print("Change access codes")

def calldivert ():
	print("""
	
	calldiverts = int(input("Enter the option"))
	match(calldiverts):
		case 1 : print("welcome to call divert")
				
def Clock():
	print("""
	1 : Alarm clock
	2 : Clock settings
	3 : Date settings
	4 : Stopwatch
	5 : Countdown timer
	6 : Auto Update date and time
		""")

	clock = int(input("pick from any options"))
	match(clock):
		case 1 : print("Alarm clock");
		case 2 : print("Clock Settings");
		case 3 : print("Date Settings");
		case 4 : print("Stopwatch");
		case 5 : print("Countdown timer");
		case 6 : print("Autoupdate Date and time");

def profiles(): 
	print("""
	1 : Profiles
	2 : Ringing volume
	3 : Set reminder
	4 : Change Background colour
		""")

	profile = int(input("enter selected options"))
	match(profile):
		case 1 : print("Profiles");
		case 2 : print("Ringing volume");
		case 3 : print("Set reminder");
		case 4 : print("Change Background colour");
		
def SIM Service():
	print("""
	1 : SIM Functions
	    """)

	sim = int(input("Enter the selected Options"))
	match(sim):
		case 1 : print("SIM Functions");

mainMenu()



