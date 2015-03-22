import praw
import csv
import time

#The strings that will 'summon' the bot:
prawWords = ['!ithkuil', 'everybody']
botusername = 'IthkuilRobot'
botuserpass = 'conlangorangutan' #SENSITIVE!!!


#What to tell reddit my bot is called.
user_agent = ("/r/ithkuil Lookup Bot 1.0 by /u/Archare")
#The reddit object
r = praw.Reddit(user_agent=user_agent)

#Login to reddit. No username or pass is given, so will prompt stdin.
r.login(username='IthkuilRobot')

#Get the abbreviations from an accompanying csv file.
#Opens the csv containing Ithkuil abbreviations to a file object.

abbrev = {}
with open('shortab.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # row[0] is the abbrev, row[1] is the map.
        abbrev[row[0]] = row[1]
abbrevkeys = abbrev.keys()
#The set of all comments already replied to.
already_done = set()

#Checks a string for ithkuil abbreviations and returns True if it does \
# and False if not.

def hasabbrev(comment):
    words = comment.split()
    for word in words:
        if word in abbrevkeys:
            return True
    return False

def replymake(comment):
    reply = []
    words = comment.split()
    for word in words:
#       Builds the words in the reply
        if word in abbrevkeys:
            reply.append(word)
            reply.append(' : ')
            reply.append(abbrev[word])
            reply.append(', ')
    rply = ''.join(reply)
    return rply

#The main loop
while True:
    submission = r.get_submission(submission_id='2zo3zb')
    flat_comment = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comment:
        op_text = comment.body.lower()
        has_praw = any(string in op_text for string in prawWords)
        #Finds the string used to invoke the bot.
        if comment.id not in already_done and has_praw:
            if hasabbrev(comment.body):
                rply = replymake(comment.body)
                comment.reply(rply)
            already_done.add(comment.id) #Tracks existing comments
    print 'Sleeping for 10s...'
    time.sleep(10)
