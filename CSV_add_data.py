import csv

with open('./test2.csv', 'a') as csv_file: #using 'a' for appened method
	user3 = ('Jim','Crow','56')
	add = csv.writer(csv_file)

	add.writerow(user3)
