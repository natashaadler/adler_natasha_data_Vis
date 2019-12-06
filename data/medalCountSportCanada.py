import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# type of sport
sports = ["Hockey", "Skating", "Curling", "Skiing", "Bobsleigh", "Biathlon"]

y_pos = np.arange(len(sports))
#number of medals won in total
medal = [351, 159, 50, 40, 22, 1]

#plots a built in method / 
plt.bar(y_pos, medal, align='center', alpha=0.5)
plt.ylabel("Total Number of Medals")
plt.xticks(y_pos, sports)
plt.xlabel("Winter Sports")
plt.title("Total Number of Medals Won by Canada per Sport")
plt.show()
