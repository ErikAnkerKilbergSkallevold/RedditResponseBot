import random
import praw
import time
import re

userAgent = ''
cID = ''
cSC= ''
userN = ''
userP ="''"
numFound = 0
reddit = praw.Reddit(user_agent=userAgent,
                    client_id=cID,
                    client_secret=cSC,
                    username=userN,
                    password=userP)
subreddit = reddit.subreddit('') #any subreddit you want to monitor e.g. Just a string like 'AHatInTime'

#index for you to keep track of
#0 aboutBot
#1 ...


responses = [[],[]] #Add responses here response[pos] must have same pos as keywords[pos]. It picks a random one 

keywords = [[],[]] #Add keywords to look for here

replied_to = []

numFound = 0
looptimer = 0

def choose_Random(response_type_in):
    response_type = response_type_in
    response_n = random.randint(0, len(responses[response_type])-1)
    chosenResponse = responses[response_type][response_n]
    #print(response_type)
    #print(chosenResponse)
    return chosenResponse

while True:
    for submission in subreddit.new(limit=30): #this views the top 30 posts in that subbreddit
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            #print(comment.score)
            if comment.author == userN and comment.score <= -1: #Deletes if downvited
                print('Bot deleting own comment: ') #replies and outputs to the command line
                print("Author: ", comment.author)
                print("Text: ", comment.body)
                print("Score: ", comment.score)
                comment.delete()
            else:
                wordCount = comment.body.lower()
                wordCountList = wordCount.split()
                wordCountNumber = len(wordCountList)
                #print("Comment text", wordCount)
                #print("Word Count:", wordCountNumber)
                #print()
                if wordCountNumber >= 4:
                    #print("Comment too long, ignoring")
                    numFound = numFound + 0
                else:
                    input = comment.body.lower()
                    inputSpaced = input.split(" ")
                    botCheck = "hatbot"
                    if botCheck not in input:
                        numFound = numFound + 0
                        #print("hatbot arg not found, ignoring")
                    else:
                        for x in inputSpaced:
                            strippedString = re.sub('\W+','', x)
                            pos1 = -1
                            for i in keywords:
                                pos1 = pos1 + 1
                                for y in i:
                                    if y == strippedString:
                                         if comment.author == userN:
                                             numFound = numFound + 0
                                            # print("Already commented by userN, ignoring")
                                         else:
                                            if comment.id in replied_to:
                                                numFound = numFound + 0
                                                #print("Comment ID found, ignoring")
                                            else:
                                                if comment.saved:
                                                    numFound = numFound + 0
                                                    #print("Comment was saved, ignoring")
                                                else:
                                                    iAmBot = '\n \n^(Beep Boop I am a bot 🤖 and this action was performed automatically. Reply with "hatbot abouthatbot2000" to get more info. -1 downvotes removes comment)'
                                                    print('Bot replying to: ') #replies and outputs to the command line
                                                    print("Author: ", comment.author)
                                                    print("Text: ", comment.body)
                                                    print("Score: ", comment.score)
                                                    print("---------------------------------")
                                                    print('Bot saying: ', choose_Random(pos1))
                                                    print()
                                                    replyString = "{}{}".format(choose_Random(pos1), iAmBot)
                                                    replied_to.append(comment.id)
                                                    comment.save()
                                                    comment.reply(replyString)
                                                    time.sleep(6)



    if numFound == 0:
        print()
        print("Sorry, didn't find any comments with those keywords, try again!")
        time.sleep(15)

    if numFound != 0:
        print()
        print("Replied to this many comments:", numFound)
        time.sleep(15)





"""
sentence = "This is a. sentence! to- test wehter this shit works!!!...!!. /timepiece "
sentenceSpaced = sentence.split(" ")
for i in sentenceSpaced:
    strippedString = re.sub('\W+','', i)
    print(strippedString)
input = sentence.lower()
inputSpaced = input.split(" ")
for x in inputSpaced:
    strippedString = re.sub('\W+','', x)
    pos1 = -1
    for i in keywords:
        pos1 = pos1 + 1
        for y in i:
            if y == strippedString:
                #print("good")
                #print(pos1)
                #print(keywords[pos1])
                print(choose_Random(pos1))
"""
