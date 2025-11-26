import csv

file = open('music.csv', 'r')
datareader = csv.reader(file, delimiter=',')
print(datareader)
