Synopsis

Biased Random number Generation Algorithm generate  the random number(s) which should be 73% biased to the higher number.
Like if I want a random number between 1 to 10 100times then it should give number more than 5 73times and less than 5 27times.
Every number generate has the probality of 73% to be lies between the Middle value & Higher Value.

Prerequisites
Python 2.7

Algorithm

	PH = 0 ; PL = 0 ; RH = 0 ; LR ; UR

	MID = (UR + LR)/2
	PH = PH + 0.73
	PL = PL + 0.27

	if PH > 1:
    		RH = random.randint (MID, UR)
    		return RN
    		PH = PH - 1


	if PL > 1:
    		RH =  random.randint (LR, MID)
    		retrun RN
    		PL = PL - 1


Explanation 

Let A is a event to occur. 
Probability of getting A

	P(A) Є [0,1]  

let say we have 100 value between 0 to 1  so get any single value, say x
we have the probability

	P(x) = 1/100

But in our case we need a number with 73% biased to higher limit.
Therfore we need to increare the probability of all number between MID to UR with 73.
PH = PH + 0.73
everything when PH >1 our algorithm generates the number from highr Bias, deduct the 1 from PH, remaining value of PH wait till it becomes complete 1 to regenrate the next value.
