import csv
import random

# First, read CSV and put the patients into ID or non ID groups

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

print ("Attempting to match %d ID patients with " % (len(Id),) +
       "%d non ID patients" % (len(nonId),))

# Make all potential matches for each ID patient:           
# Match on Ageatassessment ([4]), Gender ([5]), Caucasian_vs_NonC ([7]),
# DiagnosisGroup ([16]), SubstanceUse ([18]), Legal_Status_Group ([20])

# Ageatassessment to be matched fuzzily by ageFuzziness - a percent of
# the IdService user's age

ageFuzzinessPercent = 20
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

print "Potential Matches: " + str(potentialSortedMatches)
potSortMatchesAmount = len(potentialSortedMatches)
print "Potential matches made: %d" % (len(potentialSortedMatches), )

# For each ID patient randomly select a matched non ID patient.
# Then remove the match group from the list of potential matches and
# also remove the non Id patient from any other potential match groups.

matchesMade = 0
finalMatches = []

while len(potentialSortedMatches) != 0:
    if len(potentialSortedMatches[0]) == 1:
        potentialSortedMatches.remove(potentialSortedMatches[0])
    else:
        IdMatched = potentialSortedMatches[0][0][4:]
        nonIdMatched = potentialSortedMatches[0][random.randint(
            1,len(potentialSortedMatches[0])-1)]
        print "ID: " + IdMatched + ", Non ID: " + nonIdMatched
        finalMatches += [[IdMatched, nonIdMatched]]
        matchesMade += 1
        potentialSortedMatches.remove(potentialSortedMatches[0])
        for matchGroup in potentialSortedMatches:
            for patient in matchGroup:
                if patient == nonIdMatched:
                    matchGroup.remove(patient)
    potentialSortedMatches = sorted(potentialSortedMatches,
                    key=lambda item:(len(item),
                                    random.sample(potentialSortedMatches,
                                                len(potentialSortedMatches))))
        
# Finally, output the amount of matches made

print "Managed to make %d matches from %d potential matches" %(
    matchesMade, potSortMatchesAmount)   
