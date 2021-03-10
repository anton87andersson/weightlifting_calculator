# Weightlifting calculator

Get the for ex. Mondays between two dates.

The calc_ladder is for making a series of lifts incresing by % for each round

For ex.

Starting at 90kg , 5 rounds and an increment of 5% per round.
	
  Round 1: 90.0kg 
  Round 2: 94.5 (increse 5% of 90.0kg)
  Round 3: 99.0 (increse 5% of 94.5kg) 
	Round 4: 103.5 (increse 5% of 99.0kg)
	Round 5: 108.0 (increse 5% of 103.5kg) .....

The normal_calc is for simple % weight calculating.
  
10 rounds , 90kg start and 5% increment. 
```p
calc_ladder(10, 90, 0.05)
```

Then to use it just simple do this:

50 % 83 kg 
```c
normal_calc(83, 50)
```
