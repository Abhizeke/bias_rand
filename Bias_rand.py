import random
from decimal import Decimal

PH=0;PL=0;RN=0

LR=input("Enter Lower limit:")
UR=input("Enter Upper limit:")
R=input("Number of random number you want to generate:")

RV=R+1
MID=(UR+LR)/2
print (LR, UR, MID, PH, PL) 
for i in range(0,RV):

	PH+=0.73
	PHR=round(PH,5)
	PL+=0.27
	PLR=round(PL,5)

	if PHR>1:
		RN=random.randint(MID,UR)
		print RN
		f = open('output.txt','a')
		f.write("HigherBias  :{}".format(RN)+ '\n')
		f.close()
		PH-=1

	if PLR>1:
		RN=random.randint(LR,MID)
		print RN
		f = open('output.txt','a')
		f.write("LowerBias  :{}".format(RN)+ '\n')
		f.close()
		PL-=1
	print ("PH:", PHR)
	print ("PL:", PLR)