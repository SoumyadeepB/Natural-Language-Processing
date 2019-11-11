#!/usr/bin/python

import os
import pickle
import re
import sys

from parse_out_email_text import parseOutText


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

"""temp_counter is a way to speed up the development--there are
thousands of emails from Sara and Chris, so running over all of them
can take a long time
temp_counter helps you only look at the first 200 emails in the list so you
can iterate your modifications quicker"""
temp_counter = True


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        #temp_counter += 1
        if temp_counter:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            emailText = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            emailText = emailText.replace("sara", "").replace("shackleton", "")
            emailText = emailText.replace("chris", "").replace("germani","")
            emailText = emailText.replace("sshacklensf", "").replace("cgermannsf","")

            ### append the text to word_data
            word_data.append(emailText)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara":
                from_data.append(0)
            if name == "chris":
                from_data.append(1)


            email.close()

print "Emails processed!"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(stop_words="english")
vect.fit_transform(word_data)
print len(vect.get_feature_names())
print vect.get_feature_names()[34597]

