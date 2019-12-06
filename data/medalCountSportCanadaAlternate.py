import matplotlib.pyplot as plt

labels = ['Hockey', 'Skating', 'Curling', 'Skiing', 'Bobsleigh', 'Biathlon']
sizes = [351, 159, 50, 40, 22, 1]
colors = ['paleturquoise', 'lightseagreen', 'darkcyan', 'cadetblue', 'teal', 'aqua' ]
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()