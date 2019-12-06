import matplotlib.pyplot as plt

#Total Number of Medals Won by Sport - Canada
#This is the Pie Chart used in my App!! 

labels = ['Hockey', 'Skating', 'Curling', 'Skiing', 'Bobsleigh', 'Biathlon']
sizes = [351, 159, 50, 40, 22, 1]
colors = ['paleturquoise', 'lightseagreen', 'darkcyan', 'cadetblue', 'teal', 'aqua' ]
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()