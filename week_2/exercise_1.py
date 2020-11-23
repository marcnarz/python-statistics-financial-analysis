import pandas as pd

die = pd.DataFrame([1, 2, 3, 4, 5, 6])

# roll two dice for multiple times
sum_of_dice = die.sample(2, replace=True).sum().loc[0]
print('Sum of dice is ', sum_of_dice)

# roll three dice for multiple times
sum_of_dice = die.sample(3, replace=True).sum().loc[0]
print('Sum of three dice is ', sum_of_dice)

# The following code mimics the roll dice game for 50 times. And the results are all stored into "Result"
# Lets try and get the results of 50 sum of faces.
trial = 50
result = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]

#print the first 10 results
print(result[:10])

