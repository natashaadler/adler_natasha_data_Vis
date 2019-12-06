import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Country 
country = ["CAN", "USA", "SWE", "FIN", "SUI", "NOR"]

y_pos = np.arange(len(country))
#number of medals won in total per country
medal = [50, 5, 33, 5, 25, 15]

#plots a built in method 
plt.bar(y_pos, medal, align='center', alpha=0.5, color="green")
plt.ylabel("Total Number of Medals")
plt.xticks(y_pos, country)
plt.xlabel("Countries")
plt.title("Total Number of Medals Won in Curling by Top 3 Countries")
plt.show()
