import csv
import random

#First, read CSV and put the patients into ID or non ID groups

Id = []
nonId = []

with open('C:/Users/tomel_000/Downloads/Generated HCR Test Data.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, dialect='excel')
    next(csvfile)
    for row in data:
        if row[17] == '1':
            Id += [row]
        else:
            nonId += [row]
