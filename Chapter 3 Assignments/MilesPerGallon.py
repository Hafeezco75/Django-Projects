MilesPerGallon = 0
MilesDriven = 0
GallonsUsed = 0
TotalMilesDriven = 0
TotalGallonsUsed = 0
mile_counter = -1

while GallonsUsed != -1:

	GallonsUsed = float(input("Enter the gallons used (-1 to end): "))

	MilesDriven = int(input("Enter the miles Driven: "))

	TotalMilesDriven += MilesDriven

	TotalGallonsUsed += GallonsUsed

	MilesPerGallon = MilesDriven / GallonsUsed

	AverageMilesDriven = TotalMilesDriven / MilesDriven

	AverageGallonsUsed = TotalGallonsUsed / GallonsUsed

	print(f'The miles/gallon for this tank was {MilesPerGallon: .2f}')

	TotalMilesPerGallon = TotalMilesDriven / TotalGallonsUsed

if GallonsUsed == -1 :
	
	AverageMilesPerGallon = TotalMilesPerGallon / MilesPerGallon

	print(f'The overall average miles/gallon was {AverageMilesPerGallon: .2f}')