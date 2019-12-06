
import numpy as np
import matplotlib.pyplot as plt 

#This graph was my first attempt but it didnt work!!!!!
#Bar graph for top ten countries over all medal count - stacked graph

N = 10
bronzeMeans = (167, 107, 127, 93, 221, 177, 97, 132, 103, 79)
silverMeans = (319, 203, 171, 97, 147, 129, 126, 77, 98, 90)
goldMeans = (167, 315, 159, 250, 66, 127, 137, 76, 79, 94)
ind = np.arange(N)
width = 0.30

p1 = plt.bar(ind, bronzeMeans, width)
p2 = plt.bar(ind, silverMeans, width, bottom=bronzeMeans)
p3 = plt.bar(ind, goldMeans, width, bottom=silverMeans)

plt.ylabel(" Total Number Of Medals Won")
plt.xlabel("Top Ten Countries")
plt.title("Top Ten Countries - Total Medal Count")
plt.xticks(ind, ("USA", "CAN", "NOR", "URS", "FIN", "SWE", "GER", "SUI", "AUT", "RUS"))
plt.yticks(np.arange(0, 660, 50))
plt.legend((p1[0], p2[0], p3[0]), ("Gold", "Silver", "Bronze"))
plt.show()
