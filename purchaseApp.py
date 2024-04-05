totalCost = 0
count = 0 
Discount = 10

print("Welcome to E-store: ")
name = str(input("Please enter Name: "))
noofitem = int(input("Please Enter number of item purchased: "))
percent = input("Please Enter percentage discount: ")

while (count <= 10):
	item = int(input("Please Enter cost for item: "))
	actualDiscount = totalCost * Discount / 100 
	discountedCost = totalCost - actualDiscount
	totalCost += item
	count = count + 1

print(f' Customer Name is ' + name)
print(f' Number of item bought: is {noofitem}')
print(f' Percentage discount: is {percent}')
print(f' Original cost: is {totalCost}')
print(f' Discounted cost: {discountedCost} (Discount applied)')
print("Thanks for your patronage!")

if (totalCost >= 200): 
	print(f' Discount is {actualDiscount}')
else :
	print('Discount: 0 (No Discount applied)')



