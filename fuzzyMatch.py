import csv
import random

#First, read CSV and put the patients into ID or non ID groups

Id = []
nonId = []

with open('C:/Users/tomel_000/Downloads/Generated HCR Test Data.csv', 'rb') \
        as csvfile:
    data = csv.reader(csvfile, dialect='excel')
    next(csvfile)
    for row in data:
        if row[17] == '1':
            Id += [row]
        else:
            nonId += [row]
            
#Match on Ageatassessment ([4]), Gender ([5]), Caucasian_vs_NonC ([7]),
#DiagnosisGroup ([16]), SubstanceUse ([18]), Legal_Status_Group ([20])

#Ageatassessment to be matched fuzzily by ageFuzziness - a percent of
#the IdService user's age

ageFuzzinessPercent = 10
aF = ageFuzzinessPercent / 100.0

matches = []

for IdServiceUser in Id:
    for nonIdServiceUser in nonId:
        if (int(IdServiceUser[4]) * (1 - aF) < int(nonIdServiceUser[4]) <
                int(IdServiceUser[4]) * (1 + aF) and
                IdServiceUser[5] == nonIdServiceUser[5] and
                IdServiceUser[7] == nonIdServiceUser[7] and
                IdServiceUser[16] == nonIdServiceUser[16] and
                IdServiceUser[18] == nonIdServiceUser[18] and
                IdServiceUser[20] == nonIdServiceUser[20]):
            matches += [[IdServiceUser[0], nonIdServiceUser[0]]]
