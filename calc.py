'''
	Weightlifting calculator

	The calc_ladder is for making a series of lifts incresing by % for each round
	For ex.
	Starting at 90kg , 5 rounds and an increment of 5% per round.
	
	Round 1: 90.0kg 
	Round 2: 94.5 (increse 5% of 90.0kg)
	Round 3: 99.0 (increse 5% of 94.5kg) 
	Round 4: 103.5 (increse 5% of 99.0kg)
	Round 5: 108.0 (increse 5% of 103.5kg) .....

	The normal_calc is for simple % weight calculating.
'''

def calc_ladder(nrOfRounds, Start, Procent):
	
	for x in range(nrOfRounds):
		newsum3 = ++x
		procentPerRound = newsum3 * Procent
		testsum = Start + (procentPerRound * Start)
		print(testsum)

def normal_calc(weight, procent):
	procent_to_deciaml = procent * 0.01
	return weight*procent_to_deciaml		


calc_ladder(10, 90, 0.05)

print(normal_calc(83, 50))


