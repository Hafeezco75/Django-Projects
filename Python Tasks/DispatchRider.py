def f():

result = 0

dispatchRiders = 500

dailyPackage = 100

basePay = 5000

successDelivery = int(input("how many successful delivery was made by the Rider: "))
    
if (successDelivery < 50):

	result = successDelivery * 160 + basePay

if (successDelivery == 50 && successDelivery <= 59):

	result = successDelivery * 200 + basePay

if (successDelivery == 60 && successDelivery <= 69):

	result = successDelivery * 250 + basePay

if (successDelivery >= 70):

	result = successDelivery * 500 + basePay

	return result:

print(def f
