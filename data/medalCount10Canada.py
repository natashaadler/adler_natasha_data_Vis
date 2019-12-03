import csv
import matplotlib.pyplot as plt 

#Total Medal Trends for Canada - Last 10 Olympic Games

#1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014
#columns 0 (year) column 4 (top 10 country)


m_1980 = 0
m_1984 = 0
m_1988 = 0
m_1992 = 0
m_1994 = 0
m_1998 = 0
m_2002 = 0
m_2006 = 0
m_2010 = 0
m_2014 = 0

categories = []

#data contains just canada in the last 10 winter olympics
with open('canada_1980-2014_medal_count.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1

		else:
			if (row[0] == "1980") and (row[4] == "CAN"):
				print("1980 Medal for Canada!")
				m_1980 += 1
			elif (row[0] == "1984") and (row[4] == "CAN"):
				print("1984 Medal for Canada!")
				m_1984 += 1
			elif (row[0] == "1988") and (row[4] == "CAN"):
				print("1988 Medal for Canada!")
				m_1988 += 1
			elif (row[0] == "1992") and (row[4] == "CAN"):
				print("1992 Medal for Canada!")
				m_1992 += 1
			elif (row[0] == "1994") and (row[4] == "CAN"):
				print("1994 Medal for Canada!")
				m_1994 += 1
			elif (row[0] == "1998") and (row[4] == "CAN"):
				print("1998 Medal for Canada!")
				m_1998 += 1
			elif (row[0] == "2002") and (row[4] == "CAN"):
				print("2002 Medal for Canada!")
				m_2002 += 1
			elif (row[0] == "2006") and (row[4] == "CAN"):
				print("2006 Medal for Canada!")
				m_2006 += 1
			elif (row[0] == "2010") and (row[4] == "CAN"):
				print("2010 Medal for Canada!")
				m_2010 += 1
			elif (row[0] == "2014") and (row[4] == "CAN"):
				print("2014 Medal for Canada!")
				m_2014 += 1

medalCounts = [m_1980, m_1984, m_1988, m_1992, m_1994, m_1998, m_2002, m_2006, m_2010, m_2014]
years = [1980, 1984,1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

plt.plot(years, medalCounts, color="red", linewidth=5.0)
plt.xlabel("Olympic Year")
plt.ylabel("Medals by Year")
plt.title("Medals Sampled Over Last Ten Olympics")
plt.show()







