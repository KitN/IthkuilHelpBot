#A script to create a dictionary of all of the abbreviations in 
# ithkuil (www.ithkuil.net) for the Reddit IthkuilHelperBot
import csv

#Opens the csv containing Ithkuil abbreviations to a file object.
abbrev = {}
with open('shortab.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # row[0] is the abbrev, row[1] is the map.
        abbrev[row[0]] = row[1]

print abbrev
