# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
 
#Total Number of Medals Won - top 10 Countries broken down by gold, silver, and bronze
#this is the graph used in the app!!!!


# y-axis in bold
rc('font', weight='bold')
 
# Values of each group
gold = [167, 315, 159, 250, 66, 127, 137, 76, 79, 94]
silver = [319, 203, 171, 97, 147, 129, 126, 77, 98, 90]
bronze = [167, 107, 127, 93, 221, 177, 97, 132, 103, 79]
 
# Heights of bars1 + bars2
bars = np.add(silver, bronze).tolist()
 
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6,7,8,9]
 
# Names of group and bar width
names = ["USA", "CAN", "NOR", "URS", "FIN", "SWE", "GER", "SUI", "AUT", "RUS"]
barWidth = 1
 
# Create gold bars (top)
plt.bar(r, gold, bottom=bars, color='#d1c92e', edgecolor='white', width=barWidth)
# Create silver (middle), on top of the third one
plt.bar(r, silver, bottom=bronze, color='#a3a39d', edgecolor='white', width=barWidth)
# Create bronze (bottom)
plt.bar(r, bronze, color='#572e10', edgecolor='white', width=barWidth)
 
#Custom title
plt.title("Top Ten Countries - Total Medal Count")

# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("Countries")

# Custom Y axis
plt.ylabel("Medal Count")
 
# Show graphic
plt.show()
