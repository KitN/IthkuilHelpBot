import praw
import time

#What to tell reddit my bot is called.
user_agent = ("/r/ithkuil Lookup Bot 1.0 by /u/Archare")
#The reddit object
r = praw.Reddit(user_agent=user_agent)

#Login to reddit. No username or pass is given, so will prompt stdin.
r.login(username='IthkuilHelpBot')

#Get the abbreviations from an accompanying csv file.
import csv
#Opens the csv containing Ithkuil abbreviations to a file object.
abbrev = {}
with open('shortab.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # row[0] is the abbrev, row[1] is the map.
        abbrev[row[0]] = row[1]

#The main loop
while True:
    submission = r.get_submission(submission_id='2t4ruz')
    flat_comment = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comment:
        if comment

    time.sleep(10)
