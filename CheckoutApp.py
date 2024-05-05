from collections import Counter

counter = 0

number = 0

unit = 0

discount = 0

subTotal = 0


items = []

price = []

quantity = []

totals = []

while counter <= 0:

	customerName = str(input("What is the customer's Name "))
      
	itemname = str(input("What did the user buy "))
       
	number = int(input("How many pieces? "))
       
	unit = int(input("How much per unit? "))

	counter += 1
        
	total =  int(number * unit)

items.append(itemname)

price.append(unit)

quantity.append(number)

totals.append(total)


itemset = str(input("Add more items? ")) 

proceed = "yes"

if itemset.lower() == "proceed":
 
	cashierName = str(input("What is the Cashier's name? "))
   
	discount = int(input("How much discount will he get: "))

print("SEMICOLON STORES")
print("MAIN BRANCH")
print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
print("TEL: 03293828343")
         
print(f"{customerName}")

print("============================================================")

print("ITEM		QTY		PRICE		TOTAL(NGN)")
  
print("------------------------------------------------------------")

result = dict(Counter(totals))

for number, unit in result.items():

	print(f"{quantity.count(number)}\t\t + {price.count(unit)}\t\t + {totals.count(total)}");
subTotal += totals.count(total)
  
costDiscount = discount * subTotal / 100;

vat = 17.50 / 100 * subTotal;

billTotal = subTotal + vat - costDiscount;
     
print("-----------------------------------------------------------")  
 
print(f"\t\t\tSub Total: \t\t{subTotal}")

print(f"\t\t\tDiscount: \t\t{costDiscount}")

print(f"\t\t\tVAT at 17.50 : \t\t{vat}")

print("============================================================");

print(f"\t\t\tBill Total:          \t{billTotal}");

print("============================================================");

print(f" THIS IS NOT A RECEIPT KINDLY PAY, {billTotal}");

print("============================================================");




