#author: mortalspirit
# -*- coding: utf-8 -*-


#imports
import tweepy, time, sys
import nltk 
import random 
from nltk.corpus import wordnet as wn

#function dec
def parseStr(string):
    string = string.replace("'", "")
    string = string.replace("[", "")
    string = string.replace("]", "")
    return string


#main
nouns = set()
adjectives = set()

#twitter api info
CONSUMER_KEY = '1234abcd...'#consumer key
CONSUMER_SECRET = '1234abcd...'#secret key
ACCESS_KEY = '1234abcd...'#access token
ACCESS_SECRET = '1234abcd...'#token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


for synset in list(wn.all_synsets(wn.ADJ)):
    #print(synset)
    for x in synset.lemma_names():
        if "_" not in x: #ensure one worded adjectives
            adjectives.add(x)    

for synset in list(wn.all_synsets('n')):
    #print(synset)
    for x in synset.lemma_names():
        if "_" not in x: #ensure one worded nouns
            nouns.add(x)
     
m = True
while m == True:
    nounString = random.sample(set(nouns), 1)
    adjString = random.sample(set(adjectives), 1)
    adjString = str(adjString)
    nounString = str(nounString)
    adjString = parseStr(adjString)
    nounString = parseStr(nounString)
    print(adjString, nounString)
    try:
        #api.update_status(adjString, nounString)
        pass
    except:
        m = False
    time.sleep(10)
    




