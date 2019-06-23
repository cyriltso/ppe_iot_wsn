import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("DATA LOGS FROM ULTRASONIC SENSOR.csv")
stats_data_sensors = df.describe()
print(stats_data_sensors)

## FOR A CATEGORICAL SERIES : IF WE LET THE CSV IN THE FORM "Distance = 70.17 cm"

#top is the most frequent value
#freq is the most common value frequency
#count is the number of values from the dataset
#unique is the number of values that are different from each other
#the first value displayed is the first value of the dataset

## FOR A NUMERICAL SERIES : IF WE PUT THE CONTENT OF THE CSV ON THE FORM "Distance /n 99.73 70.14 etc..."
#mean is the usual average of a series (moyenne)
#std is the variation of a series (écart-type)
#min is the minimal value of the serie (minimum) and max is the maximal value of the serie (maximum)
#25% is the first quartile (1er quartile),
# it means that at least 25% of the serie's value are inferior or equal to this value
#50% is the median of the serie (médiane)
# it means that at least 50% of the serie's value are inferior or equal to this value
#75% is the third quartile (3ème quartile)
# it means that at least 75% of the serie's value are inferior or equal to this value
