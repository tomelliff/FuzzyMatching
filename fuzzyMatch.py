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

# Make all potential matches for each ID patient:
            
# Match on Ageatassessment ([4]), Gender ([5]), Caucasian_vs_NonC ([7]),
# DiagnosisGroup ([16]), SubstanceUse ([18]), Legal_Status_Group ([20])

# Ageatassessment to be matched fuzzily by ageFuzziness - a percent of
# the IdService user's age

ageFuzzinessPercent = 10
aF = ageFuzzinessPercent / 100.0

matches = []
onlyMatches = []

for IdServiceUser in Id:
    matches += [["ID: " + IdServiceUser[0]]]
    for nonIdServiceUser in nonId:
        if (int(IdServiceUser[4]) * (1 - aF) < int(nonIdServiceUser[4]) <
                int(IdServiceUser[4]) * (1 + aF) and
                IdServiceUser[5] == nonIdServiceUser[5] and
                IdServiceUser[7] == nonIdServiceUser[7] and
                IdServiceUser[16] == nonIdServiceUser[16] and
                IdServiceUser[18] == nonIdServiceUser[18] and
                IdServiceUser[20] == nonIdServiceUser[20]):
            matches[len(matches)-1] += [nonIdServiceUser[0]]
    if len(matches[len(matches)-1])-1 != 0:
        onlyMatches += [matches[len(matches)-1]]

potentialSortedMatches = sorted(onlyMatches,
                       key=lambda item:(len(item),
                                        random.sample(onlyMatches,
                                                      len(onlyMatches))))

print potentialSortedMatches
print "Potential matches made: %d" % (len(potentialSortedMatches), )

#For each ID patient randomly select a matched non ID patient
"""
for matchGroup in potentialSortedMatches:
    IdMatched = matchGroup[0][4:]
    nonIdMatched = matchGroup[random.randint(1,len(matchGroup)-1)]
    print IdMatched, nonIdMatched
"""
if potentialSortedMatches != 0:
    IdMatched = potentialSortedMatches[0][0][4:]
    nonIdMatched = potentialSortedMatches[0][random.randint(
        1,len(potentialSortedMatches[0])-1)]
    print "ID: " + IdMatched + ", Non ID: " + nonIdMatched
    for matchGroup in potentialSortedMatches:
        if matchGroup[0][4:] == IdMatched:
            print "This should be removed: " + str(matchGroup)
        else:
            for nonIdPatient in matchGroup[1:]:
                if nonIdPatient == nonIdMatched:
                    print "This should also be removed: " + str(matchGroup)
