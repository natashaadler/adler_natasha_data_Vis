import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Country 
country = ["CAN", "USA", "SWE", "FIN", "URS", "RUS", "SUI", "GER", "AUT", "NOR"]

y_pos = np.arange(len(country))
#number of medals won in total per country
medal = [159, 179, 20, 26, 104, 79, 3, 54, 31, 83]

#plots a built in method 
plt.bar(y_pos, medal, align='center', alpha=0.5, color="red")
plt.ylabel("Total Number of Medals")
plt.xticks(y_pos, country)
plt.xlabel("Countries")
plt.title("Total Number of Medals Won in Skating by Top 3 Countries")
plt.show()
